from env import *

# Radici p(z)
z1 = np.float64((1+np.sqrt(5))/2)
z2 = np.float64((1-np.sqrt(5))/2)

# Condizioni iniziali
c0 = np.float64(1.)
c1 = np.float64((1-sqrt(5))/2)
print("Condizioni iniziali")
print("z1=%s, z2=%s" % (float_format(z1),float_format(z2)))
print("c0=%s, c1=%s" % (float_format(c0),float_format(c1)))
print("\n")

# Soluzione Ca = c mediante matrice inversa
# (lapack corregge automaticamente certi errori di approssimazione
# nella risoluzione, in questo caso dando come soluzioni del sistema Ca=c
# esattamente 1. e 0.)

C = np.array([[1., 1.],
             [z1, z2]])
c = np.array([c0, c1])
Cinv = np.array([[-z2/(z1-z2), 1/(z1-z2)],
                    [-z1/(z2-z1), 1/(z2-z1)]])
Cinv_x_C = np.dot(Cinv, C)
a1_64, a2_64 = np.dot(Cinv, c)

print("64 bit\n", end=' ')
print("C:\n", C)
print("Cinv:\n", Cinv)
print("Cinv_x_C:\n", Cinv_x_C)
print(("Coefficienti 64 bit:\na1: %s\na2: %s\n%s" % (float_format(a1_64), float_format(a2_64), type(a2_64))))
print("\n")

C = C.astype('float32')
c = c.astype('float32')
Cinv.astype('float32')
a1_32, a2_32 = np.dot(Cinv, c).astype('float32')

print("32 bit\n", end=' ')
print("C:\n", C)
print("Cinv:\n", Cinv)
print("Cinv_x_C:\n", np.dot(Cinv, C))
print(("Coefficienti 32 bit:\na1: %s\na2: %s\n%s" % (float_format(a1_32), float_format(a2_32), type(a2_32))))
print("\n")


# Soluzione equazione
def y32(n):
    return  a1_32 * np.float32((1+sqrt(5))/2) ** n - a2_32 * np.float32((1-sqrt(5))/2) ** n
def y64(n):
    return  a1_64 * ((1+sqrt(5))/2) ** n - a2_64 * ((1-sqrt(5))/2) ** n

n_max = 50
plot_32 = [abs(y32(x)) for x in range(n_max)]
plot_64 = [abs(y64(x)) for x in range(n_max)]
plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
plt.plot(list(range(n_max)), plot_32, 'ro', color='blue', label='float32')
plt.plot(list(range(n_max)), plot_64, 'rx', color='red', label='float64')
plt.yscale('log')
plt.grid(**GRID_OPTIONS)
plt.legend(loc='upper center')
plt.xlabel('n')
plt.ylabel('$\log_{10} |y_n|$')
plt.savefig('./figs/02-fibonacci.eps', dpi=SAVE_FIG_DPI)
plt.show()
