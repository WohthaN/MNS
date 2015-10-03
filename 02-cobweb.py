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

def plot_cobweb(base, P, S, D, Sfun, Dfun, fname):
    plt.figure()
    plt.plot(base, P, label='P')
    plt.plot(base, S, label='S')
    plt.plot(base, D, label='D')
    plt.legend(loc='upper right',prop={'size':12})
    plt.ylabel('Prezzo/Domanda/Offerta')
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
    plt.quiver(pbase[:-1], pvals[:-1], pbase_diff, pvals_diff,scale_units='xy', angles='xy', scale=1)
    linebase = np.arange(Pmin-border, Pmax+border, 0.5)
    plt.plot(linebase, [Sfun(x) for x in linebase], label='S')
    plt.plot(linebase, [Dfun(x) for x in linebase], label='D')
    plt.legend(loc='upper right',prop={'size':12})
    plt.xlabel('Prezzo')
    plt.ylabel('Domanda/Offerta')
    plt.grid(GRID_OPTIONS)
    plt.savefig('./figs/02-cobweb-%s.eps'%fname, dpi=1200)

base, P, S, D, Sfun, Dfun = cobweb(100,0.25, 10,0.15, 10,10)
plot_cobweb(base, P, S, D, Sfun, Dfun, 'stable')

base, P, S, D, Sfun, Dfun = cobweb(100,0.25, 10,0.25, 10,10)
plot_cobweb(base, P, S, D, Sfun, Dfun, 'pendolum')

base, P, S, D, Sfun, Dfun = cobweb(100,0.20, 10,0.25, 10,10)
plot_cobweb(base, P, S, D, Sfun, Dfun, 'divergent')

#plt.show()
