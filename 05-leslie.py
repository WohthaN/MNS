from env import *

def plot_histogram(data, t, zlog=True):
    cg = color_map_generator(len(data), repeat=1, cmap='plasma')
    fig = plt.figure(figsize=FIG_SIZE_3D, dpi=FIG_DPI_3D)
    plt.grid(**GRID_OPTIONS)
    ax = fig.add_subplot(111, projection='3d')
    if zlog:
        ax.set_zscale('log')

    for i,d in enumerate(data):
        xs = range(0, len(d) * t, t)
        ys = [i*t]
        ax.plot_wireframe(xs, ys, d, rstride=1, cstride=0, color=cg.next(), linewidth=0.5)

    cg = color_map_generator(len(data[0]), repeat=1, cmap='copper')
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
    print np.arange(0, t * (len(alphas)), t)
    plt.twinx()
    plt.bar(np.arange(t, t * len(betas) + 1, t), betas, color='green', align='center',
            width=barwidth, linewidth=0)
    plt.ylabel('Survival')

def plot_and_save(L,m,alphas,betas,x,name,zlog=True,iterations=150):
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
# 0-1: 684.5
# 1-4: 28.6
# 5-14: 15.3
# 15-24: 79.9
# 25-34: 104.9
# 35-44: 184.4
# 45-54: 420.9
# 55-64: 877.7
# 65-74: 2011.3
# 75-84: 5011.6
# 85-100: 12.946.5

#Birth rates for 2013 USA http://www.childtrends.org/wp-content/uploads/2014/07/79_fig2.jpg
# scale 1000 (beware: women only!)
# [[0,10,0],
# [10,15,0.3],
# [15,19,26.5],
# [19,25,80.7],
# [25,30,105.5],
# [30,35,98.0],
# [35,40,49.3],
# [40,45,10.4],
# [45,55,0.8],
# [55,200,0],]


def rescale_distribution(base_distrib, n_bins):
    # Given a histrogram distribution with non-uniform bins,
    # rescale the distribution to be represented with a different
    # number of bins, in such a way that the integral of the
    # distribution remains unchanged.

def get_survival_rate(ymin,ymax):
    #compute average survivale rate for age range
    mortality = [[0,1, 684.5],
                 [1,5, 28.6],
                 [5,15, 15.3],
                 [15,25, 79.9],
                 [25,35, 104.9],
                 [35,45, 184.4],
                 [45,55, 420.9],
                 [55,65, 877.7],
                 [65,75, 2011.3],
                 [75,85, 5011.6],
                 [85,101, 12946.5],]
    mscale = 100000
    mrate = 0
    for y in range(ymin, ymax):
        for rg in mortality:
           if y >= rg[0] and y < rg[1]:
                mrate += rg[2]
    mrate = mrate / (ymax-ymin)
    return 1. - (mrate / mscale)

def get_birth_rate(ymin,ymax):
    #compute average birthrate for age range
    births = [[0,10,0],
             [10,15,0.3],
             [15,19,26.5],
             [19,25,80.7],
             [25,30,105.5],
             [30,35,98.0],
             [35,40,49.3],
             [40,45,10.4],
             [45,55,0.8],
             [55,101,0],]
    bscale = 2*1000 #assuming it taske one womand and one man to make a child
    brate = 0
    for y in range(ymin, ymax):
        for rg in births:
           if y >= rg[0] and y < rg[1]:
                brate += rg[2]
    brate = brate / (ymax-ymin)
    return brate / bscale

total_human_population = 50*10e6

#Realistic 1y/group
L = 100
m = 100
t = L/m
betas = [get_survival_rate(x,x+t) for x in np.arange(t, L, t)]
alphas = [get_birth_rate(x,x+t) for x in np.arange(0, L, t)]
print betas, len(betas)
print alphas, len(alphas)
assert len(alphas) == m
x = np.ones(m)*total_human_population/m
plot_and_save(L,m,alphas,betas,x,'Realistic 1y/group',iterations=500)

#Realistic 5y/group
L = 100
m = 20
t = L/m
betas = [get_survival_rate(x,x+t) for x in np.arange(t, L, t)]
alphas = [get_birth_rate(x,x+t) for x in np.arange(0, L, t)]
print betas, len(betas)
print alphas, len(alphas)
assert len(alphas) == m
x = np.ones(m)*total_human_population/m
plot_and_save(L,m,alphas,betas,x,'Realistic 5y/group',iterations=100)


#Realistic 10y/group
L = 100
m = 10
t = L/m
betas = [get_survival_rate(x,x+t) for x in np.arange(t, L, t)]
alphas = [get_birth_rate(x,x+t) for x in np.arange(0, L, t)]
print betas, len(betas)
print alphas, len(alphas)
assert len(alphas) == m
x = np.ones(m)*total_human_population/m
plot_and_save(L,m,alphas,betas,x,'Realistic 10y/group',iterations=50)

#Bir
# L = 100
# m = 10
#
# betas = [0.99999,
#         0.99999,
#         0.9999,
#         0.9990,
#         0.9950,
#
#         0.990,
#         0.85,
#         0.65,
#         0.5
#         ]
#
# alphas = [0.,
#         0./1000,
#         0./5,
#         0./1,
#         0./5,
#
#         0./1000,
#         0.,
#         0.,
#         0.,
#         2.5]
# x = np.ones((L/m))*10e6
# plot_and_save(L,m,alphas,betas,x,'bla')
plt.show()
