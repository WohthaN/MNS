from env import *
from cobweb_ext_utils import plot_cobweb

def cobweb_ext(d0, a, s0, b, p0, p1, r, steps):
    base = list(range(steps))
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

    return list(range(steps+1)), P, S, D, Sfun, Dfun

def check_stability(a,b,r):
    r_cond_1 = 0.5 * ((a/b)-1)
    r_cond_2 = abs(r) * b/a
    chk1 = r<r_cond_1
    chk2 = r_cond_2<1
    print("Check stabilita: a=%s, b=%s, rho=%s" % (a,b,r))
    print(" : %s < %s: %s" % (r, r_cond_1, chk1))
    print(" : %s < 1: %s "% (r_cond_2, chk2))
    print("Stabile: %s" % (chk1 and chk2))

d0, a, s0, b, p0, p1, r = 200, 0.15, 120, 0.07, 500, 490, 0.2
base, P, S, D, Sfun, Dfun = cobweb_ext(d0, a, s0, b, p0, p1, r, 10)
plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-ext-stable', 10)
check_stability(a,b,r)

d0, a, s0, b, p0, p1, r = 200, 0.15, 120, 0.07, 500, 490, 0.7
base, P, S, D, Sfun, Dfun = cobweb_ext(d0, a, s0, b, p0, p1, r, 10)
plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-ext-inst-rho', 10)
check_stability(a,b,r)

d0, a, s0, b, p0, p1, r = 200, 0.15, 120, 0.07, 500, 490, 0.
base, P, S, D, Sfun, Dfun = cobweb_ext(d0, a, s0, b, p0, p1, r, 10)
plot_cobweb(base, P, S, D, Sfun, Dfun, '02-cobweb-ext-inst-rhozero', 10)
check_stability(a,b,r)

#plt.show()
