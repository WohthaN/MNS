from env import *


def plot_armamenti(V, h, label, fname):
    time = h*np.arange(len(V))
    x = [i.item(0,0) for i in V]
    y = [i.item(1,0) for i in V]

    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.plot(time, x,color='blue', label='x')
    plt.plot(time, y, color='red', label='y')
    plt.legend(loc='upper right')
    plt.xlabel(label)
    plt.ylabel('liv. armamenti')
    plt.grid(**GRID_OPTIONS)
    plt.savefig('./figs/05-armamenti-%s.eps' % fname, dpi=SAVE_FIG_DPI)


def armamenti_eulero_esplicito(a, b, c, d, xi, eta, x0, y0, h, T):
    #y_n+1 - y_n = h f_n
    A = np.matrix([[-a,b],[c,-d]])
    f = np.matrix([[xi],[eta]])

    res = [np.matrix([[x0],[y0]])]

    n_iter = int(T/h)

    for i in range(n_iter):
        y_n = res[i] + h*(A.dot(res[i]) + f)
        res.append(y_n)

    return res


def armamenti_eulero_implicito(a, b, c, d, xi, eta, x0, y0, h, T):
    #y_n+1 - y_n = h f_n
    A = np.matrix([[-a,b],[c,-d]])
    S = (np.matrix(np.identity(2)) - h*A)**-1
    f = np.matrix([[xi],[eta]])

    res = [np.matrix([[x0],[y0]])]

    n_iter = int(T/h)

    for i in range(n_iter):
        y_n = S * (res[i]+h*f)
        res.append(y_n)

    return res



xi,eta = 1.6,1.4
x0,y0,T = 5,0.5,7
a,b,c,d = 2,1,1,2
h=0.01
V = armamenti_eulero_esplicito(a, b, c, d, xi, eta, x0, y0, h, T)
plot_armamenti(V,h,r"$a=%s,b=%s,c=%s,d=%s,\xi=%s,\eta=%s,x_0=%s,y_0=%s,h=%s$, espl." % (a,b,c,d,xi,eta,x0,y0,h),
               "espl_conv")

V = armamenti_eulero_implicito(a, b, c, d, xi, eta, x0, y0, h, T)
plot_armamenti(V,h,r"$a=%s,b=%s,c=%s,d=%s,\xi=%s,\eta=%s,x_0=%s,y_0=%s,h=%s$, impl." % (a,b,c,d,xi,eta,x0,y0,h),
               "impl_conv")

x0,y0 = 0.5,5
V = armamenti_eulero_implicito(a, b, c, d, xi, eta, x0, y0, h, T)
plot_armamenti(V,h,r"$a=%s,b=%s,c=%s,d=%s,\xi=%s,\eta=%s,x_0=%s,y_0=%s,h=%s$, impl." % (a,b,c,d,xi,eta,x0,y0,h),
               "impl_conv_2")

x0,y0 = 5,0.5
h = 0.7
V = armamenti_eulero_esplicito(a, b, c, d, xi, eta, x0, y0, h, T)
plot_armamenti(V,h,r"$a=%s,b=%s,c=%s,d=%s,\xi=%s,\eta=%s,x_0=%s,y_0=%s,h=%s$, espl." % (a,b,c,d,xi,eta,x0,y0,h),
               "espl_m_div")

V = armamenti_eulero_implicito(a, b, c, d, xi, eta, x0, y0, h, T)
plot_armamenti(V,h,r"$a=%s,b=%s,c=%s,d=%s,\xi=%s,\eta=%s,x_0=%s,y_0=%s,h=%s$, impl." % (a,b,c,d,xi,eta,x0,y0,h),
               "impl_m_div")

a,b,c,d = 0.9,2,1,2
h = 0.01
V = armamenti_eulero_implicito(a, b, c, d, xi, eta, x0, y0, h, T)
plot_armamenti(V,h,r"$a=%s,b=%s,c=%s,d=%s,\xi=%s,\eta=%s,x_0=%s,y_0=%s,h=%s$, impl." % (a,b,c,d,xi,eta,x0,y0,h),
               "impl_div")

x0,y0 = 0.5,5
V = armamenti_eulero_implicito(a, b, c, d, xi, eta, x0, y0, h, T)
plot_armamenti(V,h,r"$a=%s,b=%s,c=%s,d=%s,\xi=%s,\eta=%s,x_0=%s,y_0=%s,h=%s$, impl." % (a,b,c,d,xi,eta,x0,y0,h),
               "impl_div_2")
#plt.show()