from env import *

quiver_samples = 25
xrange = [-6,6, quiver_samples]
yrange = [-6,6, quiver_samples]

def quivplot(xrange,yrange, dx, dy):
    bx = np.linspace(*xrange)
    by = np.linspace(*yrange)
    Bx, By = np.meshgrid(bx,by)
    Bxp, Byp = np.meshgrid(dx(bx),dy(by))
    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.grid(**GRID_OPTIONS)
    plt.ylabel('$\gamma_2(t)$')
    plt.xlabel('$\gamma_1(t)$')
    plt.quiver(Bx,By,Bxp,Byp, width=0.001, scale_units='xy', pivot='tip', angles='xy', color='grey')
    plt.grid(**GRID_OPTIONS)
    pass

def add_f_to_quivplot_case_1(xrange, yrange, trange, x, y, x0, y0):
    cg = color_map_generator(trange[2], repeat=1, cmap='plasma')
    t = np.linspace(*trange)
    xv = x(x0,t)
    yv = y(y0,t)
    for s in range(len(t)-1):
        plt.plot([xv[s],xv[s+1]],[yv[s],yv[s+1]],color=cg.next(),linewidth=1)

def l_not_semisimple_basic_plot():
    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.ylabel('$\gamma_2(t)$')
    plt.xlabel('$\gamma_1(t)$')
    plt.grid(**GRID_OPTIONS)


def add_f_to_l_not_semisimple(xrange, yrange, trange, x, y, x0, y0):
    cg = color_map_generator(trange[2], repeat=1, cmap='plasma')
    t = np.linspace(*trange)
    xv = x(x0,t)
    yv = y(y0,x0,t)
    for s in range(len(t)-1):
        plt.plot([xv[s],xv[s+1]],[yv[s],yv[s+1]],color=cg.next(),linewidth=1)

#Caso 1: l1 != l2
#l1,l2 < 0: stabile

# l1 = -1
# l2 = -3
# x = lambda x0,t: x0*np.exp(l1*t)
# y = lambda y0,t: y0* np.exp(l2*t)
# dx = lambda t: l1 * t
# dy = lambda t: l2 * t
# quivplot(xrange,yrange, dx, dy)
# for sx in np.linspace(-5,5,6):
#     for sy in np.linspace(-5,5,6):
#         add_f_to_quivplot_case_1(xrange, yrange, [0, 2, 100], x, y, sx, sy)
# plt.title('$\lambda_1, \lambda_2 < 0$')
#
#
# #Caso 1: l1 != l2
# #l1,l2 > 0: instabile
#
# l1 = 1
# l2 = 3
# x = lambda x0,t: x0*np.exp(l1*t)
# y = lambda y0,t: y0* np.exp(l2*t)
# dx = lambda t: l1 * t
# dy = lambda t: l2 * t
# quivplot(xrange,yrange, dx, dy)
# for sx in np.linspace(-0.5,0.5,6):
#     for sy in np.linspace(-0.1,0.1,6):
#         add_f_to_quivplot_case_1(xrange, yrange, [0, 1.35, 100], x, y, sx, sy)
# plt.title('$\lambda_1, \lambda_2 > 0$')
#
# #Caso 1: l1 != l2
# #sign(l1) != sign(l2) > 0: sella
#
# l1 = 1
# l2 = -3
# x = lambda x0,t: x0*np.exp(l1*t)
# y = lambda y0,t: y0* np.exp(l2*t)
# dx = lambda t: l1 * t
# dy = lambda t: l2 * t
# quivplot(xrange,yrange, dx, dy)
# for sx in np.linspace(-1,1,6):
#     for sy in np.linspace(-5,5,6):
#         add_f_to_quivplot_case_1(xrange, yrange, [0, 1.7, 100], x, y, sx, sy)
# plt.title("$sign(\lambda_1)  \\neq sign(\lambda_2)$")

##Caso 2: l1 = l2
## l semisemplice < 0
# l = -2
# x = lambda x0,t: x0*np.exp(l*t)
# y = lambda y0,t: y0* np.exp(l*t)
# dx = lambda t: l * t
# dy = lambda t: l * t
# quivplot(xrange,yrange, dx, dy)
# for sx in np.linspace(-5,5,6):
#     for sy in np.linspace(-5,5,6):
#         add_f_to_quivplot_case_1(xrange, yrange, [0, 2, 100], x, y, sx, sy)
# plt.title('$\lambda<0$ semisemplice')

## l semisemplice > 0
# l = 2
# x = lambda x0,t: x0*np.exp(l*t)
# y = lambda y0,t: y0* np.exp(l*t)
# dx = lambda t: l * t
# dy = lambda t: l * t
# quivplot(xrange,yrange, dx, dy)
# for sx in np.linspace(-0.1,0.1,6):
#     for sy in np.linspace(-0.5,0.5,6):
#         add_f_to_quivplot_case_1(xrange, yrange, [0, 1.2, 100], x, y, sx, sy)
# plt.title('$\lambda>0$ semisemplice')


def l_not_semisimple_quiver(xrange, yrange, x, y):
    pass

# l < 0
# l_not_semisimple_basic_plot()
# l = -0.1
# x = lambda x0,t: x0*np.exp(l*t)
# y = lambda y0,x0,t: (y0+x0*t)*np.exp(l*t)
# for sx in np.linspace(-5,5,6):
#     for sy in np.linspace(-5,5,6):
#         add_f_to_l_not_semisimple(xrange, yrange, [0, 30, 100], x, y, sx, sy)
# plt.title('$\lambda<0$ non semisemplice')

# l > 0
l_not_semisimple_basic_plot()
l = 0.1
x = lambda x0,t: x0*np.exp(l*t)
y = lambda y0,x0,t: (y0+x0*t)*np.exp(l*t)
for sx in np.linspace(-0.1,0.1,6):
    for sy in np.linspace(-0.1,0.1,6):
        add_f_to_l_not_semisimple(xrange, yrange, [0, 10, 100], x, y, sx, sy)
plt.title('$\lambda<0$ non semisemplice')

##Caso 3: complessi coniugati



plt.show()
