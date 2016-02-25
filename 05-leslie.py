from env import *

def plot_histogram(data, t, zlog=True):
    cg = color_map_generator(len(data), repeat=1, cmap='inferno')
    fig = plt.figure(figsize=FIG_SIZE_3D, dpi=FIG_DPI_3D)
    plt.grid(**GRID_OPTIONS)
    ax = fig.add_subplot(111, projection='3d')
    if zlog:
        ax.set_zscale('log')

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

def plot_shade(data, t, zlog=True):
    if zlog:
        norm=mpl.colors.LogNorm()
    else:
        norm=mpl.colors.NoNorm()
    data = np.array(data).transpose()
    cmap = plt.cm.viridis
    fig = plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.grid(**GRID_OPTIONS)
    im = plt.imshow(data, aspect='auto', cmap=cmap, interpolation='bicubic',
                    extent=[0, len(data[0]), len(data) * t, 0], norm=mpl.colors.LogNorm())
    cbar = fig.colorbar(im)

    #Shaded plot is nicer to the eye
    im.remove()
    ls = LightSource(-90, 60)
    rgb = ls.shade(data, cmap, blend_mode='soft',norm=mpl.colors.LogNorm())
    plt.imshow(rgb, aspect='auto', cmap=cmap, interpolation='bicubic',
               extent=[0, len(data[0])*t, len(data) * t, 0], norm=mpl.colors.LogNorm())

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

def plot_and_save(L,m,alphas,betas,x,name,zlog=True,iterations=150):
    print "Computing %s" % name
    t = L/m
    plot_rates(alphas, betas, t, name)
    plt.title(name)
    #plt.savefig('./figs/05-leslie-d-%s.eps' %name, dpi=SAVE_FIG_DPI)
    r = leslie(L,m,alphas,betas,x,iterations)
    plot_histogram(r,t,zlog)
    plt.title(name)
    #plt.savefig('./figs/05-leslie-h-%s.eps' %name, dpi=SAVE_FIG_DPI)
    plot_shade(r, t, zlog)
    plt.title(name)
    #plt.savefig('./figs/05-leslie-s-%s.eps'%name, dpi=SAVE_FIG_DPI)

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
# centers for disease control and prevention
# scale: 100000
human_mortality_base = 2.5 * 10e6
human_mortality_rates = np.array([[0,1, 29138.],
                                 [1,5, 4703.],
                                 [5,15, 6147.],
                                 [15,25, 33982.],
                                 [25,35, 42572.],
                                 [35,45, 79606.],
                                 [45,55, 184686.],
                                 [55,65, 287110.],
                                 [65,75, 389238.],
                                 [75,85, 652682.],
                                 [85,100, 713647.],])
human_mortality_rates[:,2] /= human_mortality_base

#Birth rates for 2013 USA  http://www.cdc.gov/nchs/births.htm
human_birth_base = 2*3.9*10e6
human_birth_rates = np.array([[0,10,0],
                             [10,15,3098.],
                             [15,19,273105.],
                             [19,25,896745.],
                             [25,30,1120777.],
                             [30,35,1036927.],
                             [35,40,483873.],
                             [40,45,109484.],
                             [45,55,8000.],
                             [55,100,0],])
human_birth_rates[:,2] /= human_birth_base


def rescale_distribution(base_distrib, n_bins):
    # Given a histrogram distribution with non-uniform bins,
    # rescale the distribution to be represented with a different
    # number of bins, in such a way that the integral of the
    # distribution remains unchanged.
    intg = sum((base_distrib[:,1]-base_distrib[:,0])*base_distrib[:,2])
    samples = list()
    for bin in base_distrib:
        for b in np.arange(bin[0],bin[1]):
            samples.append((b,bin[2]))
    samples = np.array(samples)
    base = np.arange(0,100,100/n_bins)
    interp = sp.interp(base, samples[:,0], samples[:,1])
    interp *= intg/sum(interp)
    return interp



#Human models. We assume Lifespan is 0-100 (bound to the distribution limits)
total_human_population = 50*10e6
L = 100

#Realistic 1y/group
m = 100
betas = 1-rescale_distribution(human_mortality_rates,m)
alphas = rescale_distribution(human_birth_rates,m)
x = np.ones(m)*total_human_population/m
# plot_and_save(L,m,alphas,betas,x,'Realistic 1y/group',iterations=200)

#Realistic 5y/group
m = 20
betas = 1-rescale_distribution(human_mortality_rates,m)
alphas = rescale_distribution(human_birth_rates,m)
x = np.ones(m)*total_human_population/m
# plot_and_save(L,m,alphas,betas,x,'Realistic 5y/group',iterations=50)

#Realistic 10y/group
m = 10
betas = 1-rescale_distribution(human_mortality_rates,m)
alphas = rescale_distribution(human_birth_rates,m)
x = np.ones(m)*total_human_population/m
# plot_and_save(L,m,alphas,betas,x,'Realistic 10y/group',iterations=25)

#Realistic 5y/group with enough births
m = 20
betas = 1-rescale_distribution(human_mortality_rates,m)
alphas = rescale_distribution(human_birth_rates,m)*3.8
x = np.ones(m)*total_human_population/m
# plot_and_save(L,m,alphas,betas,x,'5y/group with enough births',iterations=100)

#population wave example
L=10
m=10
betas = np.array([0.8]*10)
alphas = np.array([0]*9+[5.])
x=np.ones(m)*10e3
# plot_and_save(L,m,alphas,betas,x,'Population wave example', iterations=100)
plt.show()
