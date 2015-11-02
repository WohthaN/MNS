from env import *

def nazione(a, r, g, y0, y1, steps):
    Y = [y0, y1]
    C = [a*y0, a*y0]
    I = [0,r * (C[1]-C[0])]
    for n in range(2,steps+2):
        cn = a*Y[n-1]
        C.append(cn)
        invn = r * (C[n]-C[n-1])
        I.append(invn)
        Y.append(cn+invn+g)

    y_eq = g/(1-a)
    return list(range(steps+2)), Y, I, C, y_eq

def plot_nazione(base,Y,I,C,y_eq,g,label,params):
    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.plot(base, Y, label='Y')
    plt.plot(base, I, label='I')
    plt.plot(base, C, label='C')
    plt.plot([0,base[-1]], [y_eq,y_eq], label='$y_{eq}$')
    plt.plot(base, [g]*len(base), label='G')
    plt.xlabel(params)
    plt.legend(loc='lower right', prop={'size':12})
    plt.grid(**GRID_OPTIONS)
    plt.savefig('./figs/02-nazione-%s.eps' %label, dpi=SAVE_FIG_DPI)

a, r, g, y0, y1 = 0.6, 0.6, 30, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 50)
plot_nazione(base,Y,I,C,y_eq,g,'stable',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))

a, r, g, y0, y1 = 0.6, 1.6, 30, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 100)
plot_nazione(base,Y,I,C,y_eq,g,'stable-hi-r',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))

a, r, g, y0, y1 = 0.9, 0.6, 30, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 130)
plot_nazione(base,Y,I,C,y_eq,g,'stable-hi-a',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))

a, r, g, y0, y1 = 1.01, 0.6, 30, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 130)
plot_nazione(base,Y,I,C,y_eq,g,'unstable-hi-a',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))

a, r, g, y0, y1 = 0.99, 1/0.99, 30, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 500)
plot_nazione(base,Y,I,C,y_eq,g,'equil',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))

a, r, g, y0, y1 = 0.99, 1.02, 30, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 500)
plot_nazione(base,Y,I,C,y_eq,g,'unstable',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))


a, r, g, y0, y1 = 0.1, 0.99/0.1, 50, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 10)
plot_nazione(base,Y,I,C,y_eq,g,'difficult',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))

a, r, g, y0, y1 = 0.1, 0.99/0.1, 43, 100, 100
base, Y, I, C, y_eq = nazione(a, r, g, y0, y1, 10)
plot_nazione(base,Y,I,C,y_eq,g,'difficult-mg',"$a=%s, r=%s, g=%s, y_0=%s, y_1=%s$"%(a, r, g, y0, y1))
#plt.show()