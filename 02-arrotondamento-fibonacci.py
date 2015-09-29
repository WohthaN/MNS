from env import *

#Radici p(z)
z1 = (1+sqrt(5))/2
z2 = (1-sqrt(5))/2
#Condizioni iniziali
c0 = 1
c1 = (1-sqrt(5))/2
c = np.array([c0, c1])
C = np.array([[ 1, 1],
              [z1,z2]])
#Soluzione Ca = c
a = np.linalg.solve(C, c)
a32 = np.linalg.solve(C.astype('float32'), c.astype('float32'))

print("Coefficienti 64 bit:\na1: %s\na2: %s" % (float_format(a[0]), float_format(a[1])))
print("Coefficienti 32 bit:\na1: %s\na2: %s" % (float_format(a32[0]), float_format(a32[1])))

#Soluzione equazione

def y(n):
    return  a[0] * ((1+sqrt(5))/2) ** n - a[1] * ((1-sqrt(5))/2) ** n

def y32(n):
    return  a32[0] * ((1+sqrt(5))/2) ** n - a32[1] * ((1-sqrt(5))/2) ** n

nmax = 40

plot_64 = [abs(y(x)) for x in range(nmax)]
plot_32 = [abs(y32(x)) for x in range(nmax)]


plt.plot(range(nmax), plot_32, color='blue')
plt.plot(range(nmax), plot_64, color='red')
plt.yscale('log')
plt.show()
