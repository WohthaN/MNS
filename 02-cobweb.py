from env import *
from cobweb_utils import plot_cobweb

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

base, P, S, D, Sfun, Dfun = cobweb(100,0.15, 10,0.10, 400,10)
plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-stable', 20)

base, P, S, D, Sfun, Dfun = cobweb(100,0.05, 10,0.05, 950,15)
plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-pendolum', 5)

base, P, S, D, Sfun, Dfun = cobweb(100,0.09, 50,0.1, 300,15)
plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-divergent', 30)

#plt.show()
