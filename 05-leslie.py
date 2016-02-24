from env import *


def plot_histogram(data,m):
    cg = color_map_generator(len(data)+1, repeat=1, cmap='plasma')
    fig = plt.figure(figsize=FIG_SIZE_3D, dpi=FIG_DPI_3D)
    plt.grid(**GRID_OPTIONS)
    ax = fig.add_subplot(111, projection='3d')
    for i,d in enumerate(data):
        xs = range(0,len(d)*m, m)
        ys = [i]
        ax.plot_wireframe(xs, ys, d, rstride=1, cstride=0, color=cg.next(), linewidth=0.5)

    cg = color_map_generator(m+1, repeat=1, cmap='prism')
    for i,d in enumerate(np.array(data).transpose()):
        xs = [m*i]
        ys = range(len(data))
        ax.plot_wireframe(xs, ys, d, rstride=1, cstride=1, color=cg.next(), linewidth=0.5, alpha=1)

def shade_plot(data,m):
    iy, ix = np.mgrid[0:len(data[0]),0:len(data)]
    data = np.array(data).transpose()

    cmap = plt.cm.viridis
    ls = LightSource(-90, 60)
    rgb = ls.shade(data, cmap, blend_mode='soft')

    fig = plt.figure(figsize=FIG_SIZE_3D, dpi=FIG_DPI_3D)
    plt.grid(**GRID_OPTIONS)
    im = plt.imshow(rgb, aspect='auto', cmap=cmap, interpolation='bicubic',
                    extent=[0,len(data[0]), len(data)*m,0])
    # # Use a proxy artist for the colorbar...
    # im = ax.imshow(data, cmap=cmap)
    # im.remove()
    cbar= fig.colorbar(im, ticks=[rgb.min(), (rgb.max()-rgb.min())/2, rgb.max()])
    cbar.ax.set_yticklabels([data.min(),(data.max()-data.min())/2,data.max()])
    # ax.set_title('Using a colorbar with a shaded plot', size='x-large')

# def plot_histogram(data,m):
#     data=np.array(data)
#     cg = color_map_generator(len(data), repeat=1, cmap='plasma')
#     fig = plt.figure(figsize=FIG_SIZE_3D, dpi=FIG_DPI_3D)
#     plt.grid(**GRID_OPTIONS)
#     ax = fig.add_subplot(111, projection='3d')
#     xs = np.ones((m, len(data))) * np.arange(0,len(data)*m,m)
#     ys = (np.ones((len(data),m)) * np.arange(m)).transpose()
#     data=data.transpose()
#     ax.plot_wireframe(xs, ys, data, rstride=1, cstride=0, color=cg.next(), linewidth=0.2)

#     xs = (np.ones((m, len(data))) * np.arange(0,len(data)*m,m))
#     ys = (np.ones((len(data),m)) * np.arange(m,0,-1)).transpose()
#     data=np.array(data).transpose()
#     ax.plot_wireframe(xs, ys, data, rstride=1, cstride=1, linewidth=0.2)


def leslie(L,m,alphas, betas, x, tsteps):
    res = [x]
    A = np.zeros((m,m))
    A[0,:] = alphas
    for i in range(1,m):
        A[i,i-1] = betas[i-1]

    for i in range(tsteps):
        res.append(np.round(np.dot(A,res[-1])))

    return res



L = 100
m = 10

betas = [0.99999,
        0.99999,
        0.9999,
        0.9990,
        0.9950,

        0.990,
        0.85,
        0.65,
        0.5
        ]

alphas = [0.,
        0./1000,
        0./5,
        0./1,
        0./5,

        0./1000,
        0.,
        0.,
        0.,
        2.5]


x = np.ones((L/m))*10e6

r = leslie(L,m,alphas,betas,x,200)
# plot_histogram(r,m)
shade_plot(r,m)
plt.show()
