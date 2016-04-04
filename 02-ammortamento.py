from env import *
PLOT_MARKER = plot_marker_generator()

# Generatore che calcola il rimanente da pagare dopo una rata
def mutuo(C, i, r, maxiter=100):
    ic = 0
    interessi = i*C
    while C+interessi-r>=0 and ic < maxiter:
        C += interessi - r
        yield (C,interessi)
        interessi = i*C
        ic+=1
    yield (C,interessi)

# Quanto deve valere una rata per estinguere dopo N pagamenti
def rata_mutuo(C, i, N):
    return (C * i)/(1-(1+i)**-N)

C = 10000
i = 0.05

# Andamento del mutuo al variare del valore della rata
plt.figure(0,figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
for r in range(480,521,5):
    m = [x[0] for x in mutuo(C,i,r)]
    plt.plot(list(range(len(m))), m, '-'+next(PLOT_MARKER), label='rata %s' % (r))
plt.legend(loc='upper left',prop={'size':12})
plt.grid(**GRID_OPTIONS)
plt.xlabel('numero rate')
plt.ylabel('Rimanente da pagare')
plt.savefig('./figs/02-ammortamento-rata.eps', dpi=SAVE_FIG_DPI)

# al variare del numero di rate
for N in [1] + list(range(10,80,10)):
    r = rata_mutuo(C,i,N)
    m = [x[1] for x in mutuo(C,i,r)]
    marker = next(PLOT_MARKER)
    plt.figure(1)
    plt.plot(list(range(len(m))), m, '-'+marker, label='n rate %s' % (N))
    plt.figure(2)
    s = np.cumsum(m)
    plt.plot(list(range(len(s))), s, '-'+marker, label='n rate %s' % (N))

plt.figure(1,figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
plt.legend(loc='upper right',prop={'size':12})
plt.grid(**GRID_OPTIONS)
plt.xlabel('numero rate')
plt.ylabel('Interessi pagati per rata')
plt.savefig('./figs/02-ammortamento-interessi.eps', dpi=SAVE_FIG_DPI)

plt.figure(2,figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
plt.legend(loc='upper left',prop={'size':12})
plt.grid(**GRID_OPTIONS)
plt.xlabel('numero rate')
plt.ylabel('Interessi totali')
plt.savefig('./figs/02-ammortamento-int-totali.eps', dpi=SAVE_FIG_DPI)

# plt.show()

