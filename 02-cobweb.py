from env import *
from itertools import chain


def cobweb(d0, a, s0, b, p0, steps):
    base = range(steps)
    d0ms0 = d0-s0
    Sfun = lambda x: b*x+s0
    Dfun = lambda x: -a*x+d0
    P = [p0]
    S = [s0]
    D = [-a*p0+d0]
    for i in base[1:]:
        P.append( (d0ms0 - b*P[i-1])/a)
        S.append(Sfun(P[i-1]))
        D.append(Dfun(P[i]))

    return base, P, S, D, Sfun, Dfun

def plot_cobweb(base, P, S, D, Sfun, Dfun, fname, n_colors):
    plt.figure()
    plt.plot(base, P, label='P')
    plt.ylabel('Prezzo')
    plt.legend(loc='lower right',prop={'size':12})
    plt.twinx()
    plt.plot(base, S, label='S', color='g')
    plt.plot(base, D, label='D', color='r')
    plt.legend(loc='upper right',prop={'size':12})
    plt.ylabel('Domanda/Offerta')
    plt.xlabel('Iterazione')
    plt.grid(GRID_OPTIONS)
    plt.savefig('./figs/02-cobweb-%s-time.eps'%fname, dpi=1200)
    plt.figure()
    pbase = list(chain(*zip(P,P[:-1])))
    pvals = list(chain(*zip(D,S[1:])))
    pbase_diff = np.diff(np.array(pbase))
    pvals_diff = np.diff(np.array(pvals))
    Pmin, Pmax = min(P), max(P)
    border = Pmax*0.1
    color_map_gen = color_map_generator(n_colors)
    colors = [color_map_gen.next() for _ in range(len(pbase_diff))]
    plt.quiver(pbase[:-1], pvals[:-1], pbase_diff, pvals_diff, color=colors, scale_units='xy', angles='xy', scale=1)
    linebase = np.arange(Pmin-border, Pmax+border, 0.5)
    plt.plot(linebase, [Sfun(x) for x in linebase], label='S')
    plt.plot(linebase, [Dfun(x) for x in linebase], label='D')
    plt.legend(loc='upper right',prop={'size':12})
    plt.xlabel('Prezzo')
    plt.ylabel('Domanda/Offerta')
    plt.grid(GRID_OPTIONS)
    plt.savefig('./figs/02-cobweb-%s.eps'%fname, dpi=1200)

base, P, S, D, Sfun, Dfun = cobweb(100,0.15, 10,0.10, 400,10)
plot_cobweb(base, P, S, D, Sfun, Dfun, 'stable', 20)

base, P, S, D, Sfun, Dfun = cobweb(100,0.05, 10,0.05, 950,15)
plot_cobweb(base, P, S, D, Sfun, Dfun, 'pendolum', 5)

base, P, S, D, Sfun, Dfun = cobweb(100,0.09, 50,0.1, 300,15)
plot_cobweb(base, P, S, D, Sfun, Dfun, 'divergent', 30)

plt.show()
