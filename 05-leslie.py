from env import *

def plot_histogram(data, t, zlog=True):
    cg = color_map_generator(len(data), repeat=1, cmap='inferno')
    fig = plt.figure(figsize=FIG_SIZE_3D, dpi=FIG_DPI_3D)
    plt.grid(**GRID_OPTIONS)
    ax = fig.add_subplot(111, projection='3d')
    if zlog:
        ax.set_zscale('log')
        data = np.log(np.array(data))

    for i,d in enumerate(data):
        xs = range(0, len(d) * t, t)
        ys = [i*t]
        ax.plot_wireframe(xs, ys, d, rstride=1, cstride=0, color=cg.next(), linewidth=0.5)

    cg = color_map_generator(len(data[0]), repeat=1, cmap='cool')
    for i,d in enumerate(np.array(data).transpose()):
        xs = [t * i]
        ys = np.arange(len(data))*t
        ax.plot_wireframe(xs, ys, d, rstride=1, cstride=1, color=cg.next(), linewidth=0.5, alpha=1)

    ax.view_init(elev=45, azim=45)
    plt.xlabel('Bin')
    plt.ylabel('Time')


def plot_shade(data, t, zlog=True):
    if zlog:
        norm=mpl.colors.LogNorm()
    else:
        norm=None

    data = np.array(data).transpose()
    cmap = plt.cm.viridis
    fig = plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.grid(**GRID_OPTIONS)
    im = plt.imshow(data, aspect='auto', cmap=cmap, interpolation='bicubic',
                    extent=[0, len(data[0]), len(data) * t, 0], norm=norm)
    cbar = fig.colorbar(im)

    #Shaded plot is nicer to the eye
    im.remove()
    ls = LightSource(-90, 60)
    rgb = ls.shade(data, cmap, blend_mode='soft',norm=norm)
    plt.imshow(rgb, aspect='auto', cmap=cmap, interpolation='bicubic',
               extent=[0, len(data[0])*t, len(data) * t, 0], norm=norm)
    plt.xlabel('Time')
    plt.ylabel('Bin')

def plot_rates(alphas, betas, t, name):
    barwidth = t/2.5
    fig = plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.grid(**GRID_OPTIONS)
    plt.bar(np.arange(0, t * (len(alphas)), t)+barwidth, alphas, color='red', align='center',
            width=barwidth, linewidth=0)
    plt.ylabel('Birthrate')
    plt.twinx()
    plt.bar(np.arange(t, t * len(betas) + 1, t), betas, color='green', align='center',
            width=barwidth, linewidth=0)
    plt.ylabel('Survival')

def plot_and_save(L,m,alphas,betas,x,name,zlog=False,iterations=150):
    print "Computing %s" % name
    savename = name.replace(' ', '_')
    t = L/m
    plot_rates(alphas, betas, t, name)
    plt.title(name)
    plt.savefig('./figs/05-leslie-d-%s.eps' %savename, dpi=SAVE_FIG_DPI)
    r = leslie(L,m,alphas,betas,x,iterations)
    plot_histogram(r,t,zlog)
    plt.title(name)
    plt.savefig('./figs/05-leslie-h-%s.eps' %savename, dpi=SAVE_FIG_DPI)
    plot_shade(r, t, zlog)
    plt.title(name)
    plt.savefig('./figs/05-leslie-s-%s.eps'%savename, dpi=SAVE_FIG_DPI)

def leslie(L,m,alphas, betas, x, tsteps):
    res = [x]
    A = np.zeros((m,m))
    A[0,:] = alphas
    for i in range(1,m):
        A[i,i-1] = betas[i-1]

    for i in range(tsteps):
        res.append(np.round(np.dot(A,res[-1])))

    return res

#Mortality rates for 2007 USA from http://www.cdc.gov/nchs/nvss/mortality/gmwk23r.htm
#http://www.cdc.gov/nchs/data/dvs/mortfinal2007_worktable23r.pdf
# centers for disease control and prevention
# scale: 100000
human_mortality_base = 1e5
human_mortality_rates = np.array([[0,1, 684.],
                                 [1,5, 29.],
                                 [5,15, 15.3],
                                 [15,25, 79.9],
                                 [25,35, 104.9],
                                 [35,45, 184.4],
                                 [45,55, 420.9],
                                 [55,65, 877.7],
                                 [65,75, 2011.3],
                                 [75,85, 5011.6],
                                 [85,100, 12946.5],])
human_mortality_rates[:,2] /= human_mortality_base

#Birth rates for 2013 USA  http://www.cdc.gov/nchs/births.htm
#http://www.cdc.gov/nchs/data/nvsr/nvsr64/nvsr64_01.pdf
#Normalized on female population per age group
human_birth_base = 2000
human_birth_rates = np.array([[0,10,0],
                             [10,15,0.3],
                             [15,19,26.5],
                             [19,25,80.7],
                             [25,30,105.5],
                             [30,35,98.],
                             [35,40,49.3],
                             [40,45,10.4],
                             [45,55,0.5],
                             [55,100,0],])
human_birth_rates[:,2] /= human_birth_base


def rescale_distribution(base_distrib, n_bins):
    # Given a histrogram distribution with non-uniform bins,
    # rescale the distribution to be represented with a different
    # number of bins and normalize it to have unitary integral.
    # Normalize the distribution.
    intg = sum((base_distrib[:,1]-base_distrib[:,0])*base_distrib[:,2])
    samples = list()
    for bin in base_distrib:
        for b in np.arange(bin[0],bin[1]):
            samples.append((b,bin[2]))
    samples = np.array(samples)
    base = np.arange(0,100,100/n_bins)
    interp = sp.interp(base, samples[:,0], samples[:,1])
    interp *= 1/(sum(interp))
    return interp



#Human models. We assume Lifespan is 0-100 (bound to the distribution limits)
total_human_population = 320*10e6
L = 100

#Realistic 1y/group
m = 100
betas = 1-rescale_distribution(human_mortality_rates,m)
alphas = rescale_distribution(human_birth_rates,m)
x = np.ones(m)*total_human_population/m
plot_and_save(L,m,alphas,betas,x,'Realistic 1y group',iterations=100)

#Realistic 5y/group
m = 20
betas = 1-rescale_distribution(human_mortality_rates,m)
alphas = rescale_distribution(human_birth_rates,m)
x = np.ones(m)*total_human_population/m
plot_and_save(L,m,alphas,betas,x,'Realistic 5y group',iterations=20)

#Realistic 10y/group
m = 10
betas = 1-rescale_distribution(human_mortality_rates,m)
alphas = rescale_distribution(human_birth_rates,m)
x = np.ones(m)*total_human_population/m
plot_and_save(L,m,alphas,betas,x,'Realistic 10y group',iterations=10)

#Ostrowski examples
L = 4
m = 4
betas = np.array([0.5]*4)
alphas_1 = np.array([0,1.5,1.5,0])
alphas_2 = np.array([0,0,1.5,1.5])
x = np.ones(m)*10e2
plot_and_save(L,m,alphas_1,betas,x,'Ostrowski 1', iterations=50, zlog=True)
x = np.ones(m)*10e8
plot_and_save(L,m,alphas_2,betas,x,'Ostrowski 2', iterations=50, zlog=True)


#population wave example
L=4
m=4
betas = np.array([0.5]*4)
alphas = np.array([0,0,0,5.])
x=np.ones(m)*10e6
plot_and_save(L,m,alphas,betas,x,'Population wave example', iterations=20, zlog=True)

# plt.show()
