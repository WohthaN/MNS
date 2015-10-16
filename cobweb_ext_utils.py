from env import *
from itertools import chain

def plot_cobweb(base, P, S, D, Sfun, Dfun, fname, n_colors):
    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.plot(base, P, label='P')
    plt.ylabel('Prezzo')
    plt.legend(loc='lower right',prop={'size':12})
    plt.grid(**GRID_OPTIONS)
    plt.twinx()
    plt.plot(base, S, label='S', color='g')
    plt.plot(base, D, label='D', color='r')
    plt.legend(loc='upper right',prop={'size':12})
    plt.ylabel('Domanda/Offerta')
    plt.xlabel('Iterazione')
    plt.grid(**GRID_OPTIONS_TWIN)
    plt.savefig('./figs/%s-time.eps'%fname, dpi=SAVE_FIG_DPI)

    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    pbase = list(chain(*zip(P,P[:-1])))
    pvals = list(chain(*zip(D,S[1:])))
    pbase_diff = np.diff(np.array(pbase))
    pvals_diff = np.diff(np.array(pvals))
    Pmin, Pmax = min(P), max(P)
    border = Pmax*0.1
    color_map_gen = color_map_generator(n_colors, repeat=2)
    colors = [color_map_gen.next() for _ in range(len(pbase_diff))]
    plt.quiver(pbase[:-1], pvals[:-1], pbase_diff, pvals_diff, color=colors, scale_units='xy', angles='xy', scale=1)
    linebase = np.arange(Pmin-border, Pmax+border, (Pmax-Pmin)/20)
    # plt.plot(linebase, [Sfun(x) for x in linebase], label='S')
    plt.plot(linebase, [Dfun(x) for x in linebase], label='D', color='red')
    plt.legend(loc='upper right',prop={'size':12})
    plt.xlabel('Prezzo')
    plt.ylabel('Domanda/Offerta')
    plt.grid(**GRID_OPTIONS)
    plt.savefig('./figs/%s.eps'%fname, dpi=SAVE_FIG_DPI)

    fig = plt.figure(figsize=FIG_SIZE_3D, dpi=FIG_DPI_3D)
    ax = fig.gca(projection='3d')
    X = linebase
    Y = linebase
    X, Y = np.meshgrid(X, Y)
    ZS = Sfun(X,Y)
    ZD = Dfun(X)
    ax.plot_wireframe(X, Y, ZS, rstride=1, cstride=1, color=(0,1,0,0.2))
    ax.plot_wireframe(X, Y, ZD, rstride=1, cstride=1, color=(1,0,0,0.2))
    ax.set_xlabel('$p_n$')
    ax.set_ylabel('$p_{n-1}$')
    ax.set_zlabel('Domanda/Offerta')
    X,Z = pbase, pvals
    Y = list(chain(*zip([P[0]]+P[:-2],[P[0]]+P)))
    color_map_gen = color_map_generator(n_colors, repeat=2)
    for i in range(1,len(X)):
        ax.plot((X[i-1],X[i]), ((Y[i-1],Y[i])), (Z[i-1],Z[i]), color=color_map_gen.next(), linewidth=2)
    ax.zaxis.set_major_locator(mpl_ticker.LinearLocator(20))
    ax.view_init(elev=35, azim=-70)
    ax.zaxis.set_major_formatter(mpl_ticker.FormatStrFormatter('%.02f'))

    plt.savefig('./figs/%s-td.eps'%fname, dpi=SAVE_FIG_DPI)
