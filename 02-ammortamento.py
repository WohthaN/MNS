from env import *

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

# Andamento del mutuo al variare della rata
plt.figure(0)
C = 10000
i = 0.05
for r in range(480,530,5):
    m = [x[0] for x in mutuo(C,i,r)]
    plt.plot(range(len(m)), m, '-'+PLOT_MARKER.next(), label='rata %s' % (r))
plt.legend(loc='upper left',prop={'size':12})
plt.xlabel('numero rate')
plt.ylabel('Rimanente da pagare')
plt.savefig('./figs/02-ammortamento-rata.eps', dpi=1200)


C = 10000
i=0.05
for N in range(1,102,20):
    r = rata_mutuo(C,i,N)
    m = [x[1] for x in mutuo(C,i,r)]
    marker = PLOT_MARKER.next()
    plt.figure(1)
    plt.plot(range(len(m)), m, '-'+marker, label='n rate %s' % (N))
    plt.figure(2)
    s = np.cumsum(m)
    plt.plot(range(len(s)), s, '-'+marker, label='n rate %s' % (N))

plt.figure(1)
plt.legend(loc='upper right',prop={'size':12})
plt.xlabel('numero rate')
plt.ylabel('Interessi pagati per rata')
plt.savefig('./figs/02-ammortamento-interessi.eps', dpi=1200)

plt.figure(2)
plt.legend(loc='upper left',prop={'size':12})
plt.xlabel('numero rate')
plt.ylabel('Interessi totali')
plt.savefig('./figs/02-ammortamento-int-totali.eps', dpi=1200)

#plt.show()

