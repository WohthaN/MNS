from env import *
# Radici p(z)
z1 = (1+sqrt(5))/2
z2 = (1-sqrt(5))/2
# Condizioni iniziali
c0 = 1
c1 = (1-sqrt(5))/2

# Soluzione Ca = c mediante matrice inversa
# (lapack corregge automaticamente certi errori di approssimazione
# nella risoluzione, in questo caso dando come soluzioni del sistema Ca=c
# esattamente 1. e 0.)

C = np.array([[1., 1.],
             [z1, z2]])
c = np.array([c0, c1])

Cinv_64 = np.linalg.inv(C)
a1_64, a2_64 = np.dot(Cinv_64, c)

Cinv_32 = np.linalg.inv(C.astype('float32'))
a1_32, a2_32 = np.dot(Cinv_32, c).astype('float32')

print("Coefficienti 32 bit:\na1: %s\na2: %s\n%s" % (float_format(a1_32), float_format(a2_32), type(a2_32)))
print("Coefficienti 64 bit:\na1: %s\na2: %s\n%s" % (float_format(a1_64), float_format(a2_64), type(a2_64)))

# Soluzione equazione
def y32(n):
    return  a1_32 * np.float32((1+sqrt(5))/2) ** n - a2_32 * np.float32((1-sqrt(5))/2) ** n
def y64(n):
    return  a1_64 * ((1+sqrt(5))/2) ** n - a2_64 * ((1-sqrt(5))/2) ** n

n_max = 50
plot_32 = [abs(y32(x)) for x in range(n_max)]
plot_64 = [abs(y64(x)) for x in range(n_max)]
plt.plot(range(n_max), plot_32, 'ro', color='blue', label='float32')
plt.plot(range(n_max), plot_64, 'rx', color='red', label='flat64')
plt.yscale('log')
plt.legend(loc='upper center')
plt.xlabel('n')
plt.ylabel('$\log_{10} |y_n|$')
plt.savefig('./figs/02-fibonacci.eps', dpi=1200)
# plt.show()
