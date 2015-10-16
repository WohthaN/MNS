from env import *
from cobweb_ext_utils import plot_cobweb

def cobweb_ext(d0, a, s0, b, p0, p1, r, steps):
    base = range(steps)
    d0ms0 = d0-s0
    b1pr = b*(1+r)
    br = b*r
    Sfun = lambda pn,pnm1: b*(pn + r * (pn-pnm1)) + s0
    Dfun = lambda pn: -a*pn+d0
    P = [p0,p1]
    S = [s0,s0]
    D = [-a*p0+d0, -a*p1+d0]
    for n in base[1:]:
        P.append( (d0ms0 - b1pr*P[n] + br *P[n-1])/a)
        S.append(Sfun(P[n],P[n-1]))
        D.append(Dfun(P[n+1]))

    return range(steps+1), P, S, D, Sfun, Dfun

base, P, S, D, Sfun, Dfun = cobweb_ext(200,0.15, 150,0.07, 500, 490, 0.3, 10)
plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-ext-stable', 10)

# base, P, S, D, Sfun, Dfun = cobweb(100,0.05, 10,0.05, 950,15)
# plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-pendolum', 8)
#
# base, P, S, D, Sfun, Dfun = cobweb(100,0.09, 50,0.1, 300,15)
# plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-divergent', 30)

plt.show()
