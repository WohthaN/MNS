from env import *
from bigfloat import sqrt, precision

n_max = 50

fib32 = [np.float32(1), np.float32((1-sqrt(5))/2)]
for i in range(0,n_max-2):
    fib32.append( np.float32(fib32[i]+fib32[i+1]))

fib64 = [np.float64(1), np.float64((1-sqrt(5))/2)]
for i in range(0,n_max-2):
    fib64.append( np.float64(fib64[i]+fib64[i+1]))

print(fib32)
print(fib64)

plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
plt.plot(list(range(n_max)), np.abs(fib32), 'ro', color='blue', label='float32')
plt.plot(list(range(n_max)), np.abs(fib64), 'rx', color='red', label='float64')
plt.yscale('log')
plt.grid(**GRID_OPTIONS)
plt.legend(loc='upper center')
plt.xlabel('n')
plt.ylabel('$\log_{10} |y_n|$')
plt.savefig('./figs/02-fibonacci-c.eps', dpi=SAVE_FIG_DPI)
#plt.show()