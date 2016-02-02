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

def add_f_to_quivplot_case_1(xrange, yrange, trange, x, y, x0, y0):
    cg = color_map_generator(trange[2], repeat=1, cmap='plasma')
    t = np.linspace(*trange)
    xv = x(x0,t)
    yv = y(y0,t)
    for s in range(len(t)-1):
        plt.plot([xv[s],xv[s+1]],[yv[s],yv[s+1]],color=cg.next(),linewidth=1)

def l_not_semisimple_quiver(xrange, yrange, dx, dy):
    bx = np.linspace(*xrange)
    by = np.linspace(*yrange)
    Bx, By = np.meshgrid(bx,by)
    Bxp = np.array([dx(bx) for _ in range(xrange[2])])
    Byp = np.array([dy(bx,t) for t in by])
    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.grid(**GRID_OPTIONS)
    plt.ylabel('$\gamma_2(t)$')
    plt.xlabel('$\gamma_1(t)$')
    plt.quiver(Bx,By,Bxp,Byp, width=0.001, scale_units='xy', pivot='tip', angles='xy', color='grey')
    plt.grid(**GRID_OPTIONS)

def add_f_to_l_not_semisimple(xrange, yrange, trange, x, y, x0, y0):
    cg = color_map_generator(trange[2], repeat=1, cmap='plasma')
    t = np.linspace(*trange)
    xv = x(x0,t)
    yv = y(y0,x0,t)
    for s in range(len(t)-1):
        if abs(xv[s+1]) <= abs(xrange[0]) and abs(yv[s+1]) <= abs(yrange[0]):
            plt.plot([xv[s],xv[s+1]],[yv[s],yv[s+1]],color=cg.next(),linewidth=1)

def l_not_real_quiver(xrange, yrange, dx, dy):
    bx = np.linspace(*xrange)
    by = np.linspace(*yrange)
    Bx, By = np.meshgrid(bx,by)
    Bxp = dx(Bx,By)
    Byp = dy(Bx,By)
    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.grid(**GRID_OPTIONS)
    plt.ylabel('$\\theta(t)$')
    plt.xlabel('$\\rho(t)$')
    plt.quiver(Bx,By,Bxp,Byp, width=0.001, scale_units='xy', pivot='tip', angles='xy', color='grey')
    plt.grid(**GRID_OPTIONS)

def add_f_to_l_not_real(xrange, yrange, trange, rho, theta, rho0, theta0):
    cg = color_map_generator(trange[2], repeat=1, cmap='plasma')
    t = np.linspace(*trange)
    r = rho(rho0,t)
    t = theta(theta0,t)
    xv = r * np.cos(t)
    yv = r * np.sin(t)
    for s in range(len(t)-1):
        if abs(xv[s+1]) <= abs(xrange[0]) and abs(yv[s+1]) <= abs(yrange[0]):
            plt.plot([xv[s],xv[s+1]],[yv[s],yv[s+1]],color=cg.next(),linewidth=1)

#Caso 1: l1 != l2
#l1,l2 < 0: stabile

l1 = -1
l2 = -3
x = lambda x0,t: x0*np.exp(l1*t)
y = lambda y0,t: y0* np.exp(l2*t)
dx = lambda t: l1 * t
dy = lambda t: l2 * t
quivplot(xrange,yrange, dx, dy)
for sx in np.linspace(-5,5,6):
    for sy in np.linspace(-5,5,6):
        add_f_to_quivplot_case_1(xrange, yrange, [0, 2, 100], x, y, sx, sy)
plt.title('$\lambda_1, \lambda_2 < 0$')
plt.savefig('./figs/05-caso1-1stabile.eps', dpi=SAVE_FIG_DPI)


#Caso 1: l1 != l2
#l1,l2 > 0: instabile

l1 = 1
l2 = 3
x = lambda x0,t: x0*np.exp(l1*t)
y = lambda y0,t: y0* np.exp(l2*t)
dx = lambda t: l1 * t
dy = lambda t: l2 * t
quivplot(xrange,yrange, dx, dy)
for sx in np.linspace(-0.5,0.5,6):
    for sy in np.linspace(-0.1,0.1,6):
        add_f_to_quivplot_case_1(xrange, yrange, [0, 1.35, 100], x, y, sx, sy)
plt.title('$\lambda_1, \lambda_2 > 0$')
plt.savefig('./figs/05-caso1-2instabile.eps', dpi=SAVE_FIG_DPI)

#Caso 1: l1 != l2
#sign(l1) != sign(l2) > 0: sella

l1 = 1
l2 = -3
x = lambda x0,t: x0*np.exp(l1*t)
y = lambda y0,t: y0* np.exp(l2*t)
dx = lambda t: l1 * t
dy = lambda t: l2 * t
quivplot(xrange,yrange, dx, dy)
for sx in np.linspace(-1,1,6):
    for sy in np.linspace(-5,5,6):
        add_f_to_quivplot_case_1(xrange, yrange, [0, 1.7, 100], x, y, sx, sy)
plt.title("$sign(\lambda_1)  \\neq sign(\lambda_2)$")
plt.savefig('./figs/05-caso1-3sella.eps', dpi=SAVE_FIG_DPI)

#Caso 2: l1 = l2
# l semisemplice < 0
l = -2
x = lambda x0,t: x0*np.exp(l*t)
y = lambda y0,t: y0* np.exp(l*t)
dx = lambda t: l * t
dy = lambda t: l * t
quivplot(xrange,yrange, dx, dy)
for sx in np.linspace(-5,5,6):
    for sy in np.linspace(-5,5,6):
        add_f_to_quivplot_case_1(xrange, yrange, [0, 2, 100], x, y, sx, sy)
plt.title('$\lambda<0$ semisemplice')
plt.savefig('./figs/05-caso2-1stabile.eps', dpi=SAVE_FIG_DPI)

# l semisemplice > 0
l = 2
x = lambda x0,t: x0*np.exp(l*t)
y = lambda y0,t: y0* np.exp(l*t)
dx = lambda t: l * t
dy = lambda t: l * t
quivplot(xrange,yrange, dx, dy)
for sx in np.linspace(-0.5,0.5,6):
    for sy in np.linspace(-0.5,0.5,6):
        add_f_to_quivplot_case_1(xrange, yrange, [0, 1.2, 100], x, y, sx, sy)
plt.title('$\lambda>0$ semisemplice')
plt.savefig('./figs/05-caso2-2instabile.eps', dpi=SAVE_FIG_DPI)

# l < 0
l = -0.6
x = lambda x0,t: x0*np.exp(l*t)
y = lambda y0,x0,t: (y0+x0*t)*np.exp(l*t)
dx = lambda tx: l*tx
dy = lambda tx,ty: l*ty+tx
l_not_semisimple_quiver([-6,6,25],[-6,6,25],dx,dy)
for sx in np.linspace(-5,5,3):
    for sy in np.linspace(-5,5,3):
        add_f_to_l_not_semisimple(xrange, yrange, [0, 10, 100], x, y, sx, sy)
plt.title('$\lambda<0$ non semisemplice')
plt.savefig('./figs/05-caso2-3stabile.eps', dpi=SAVE_FIG_DPI)

# l > 0
l = 0.6
x = lambda x0,t: x0*np.exp(l*t)
y = lambda y0,x0,t: (y0+x0*t)*np.exp(l*t)
dx = lambda tx: l*tx
dy = lambda tx,ty: l*ty+tx
l_not_semisimple_quiver([-6,6,25],[-6,6,25],dx,dy)
for sx in np.linspace(-0.015,0.015,2):
    for sy in np.linspace(-0.16,0.16,8):
        add_f_to_l_not_semisimple(xrange, yrange, [0, 10, 100], x, y, sx, sy)
plt.title('$\lambda>0$ non semisemplice')
plt.savefig('./figs/05-caso2-4instabile.eps', dpi=SAVE_FIG_DPI)

#Caso 3: complessi coniugati
# divergente: a>0
a = 1
b = -3
rho = lambda rho0,t: rho0*np.exp(a*t)
theta = lambda theta0,t: theta0+b*t
dx = lambda tx,ty: a*tx-b*ty
dy = lambda tx,ty: a*ty+b*tx
l_not_real_quiver(xrange, yrange, dx, dy)
for sr in np.linspace(-0.5,0.5,3):
    for st in np.linspace(-0.5,0.5,3):
        add_f_to_l_not_real(xrange, yrange, [0, 2*np.pi, 100], rho, theta, sr, st)
plt.savefig('./figs/05-caso3-1div.eps', dpi=SAVE_FIG_DPI)

# conv: a<0
# b stabilisce la velocita' e il senso di rotazione
a = -1
b = 2
rho = lambda rho0,t: rho0*np.exp(a*t)
theta = lambda theta0,t: theta0+b*t
dx = lambda tx,ty: a*tx-b*ty
dy = lambda tx,ty: a*ty+b*tx
l_not_real_quiver(xrange, yrange, dx, dy)
for sr in np.linspace(-5,5,3):
    for st in np.linspace(-5,5,3):
        add_f_to_l_not_real(xrange, yrange, [0, 2*np.pi, 100], rho, theta, sr, st)
plt.savefig('./figs/05-caso3-2conv.eps', dpi=SAVE_FIG_DPI)

# circle: a=0
a = 0
b = 1
rho = lambda rho0,t: rho0*np.exp(a*t)
theta = lambda theta0,t: theta0+b*t
dx = lambda tx,ty: a*tx-b*ty
dy = lambda tx,ty: a*ty+b*tx
l_not_real_quiver(xrange, yrange, dx, dy)
for sr in np.linspace(-5,0.1,10):
        add_f_to_l_not_real(xrange, yrange, [0, 2*np.pi, 100], rho, theta, sr, sr)
plt.savefig('./figs/05-caso3-3circ.eps', dpi=SAVE_FIG_DPI)
# plt.show()
