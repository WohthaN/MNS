from env import *

def plot(MIN, MAX, h):

    tbase = np.arange(MIN, MAX, h)
    MAXITERS = int((MAX - MIN) / h) - 2

    exact_solution = [5 / (1 + 4 * exp(-10 * x)) for x in tbase]

    y = [1, 5 / (1 + 4 * exp(-10*(MIN+h)))]
    for i in range(MAXITERS):
        y.append(2*h*(10*y[i+1]-2*y[i+1]**2)+y[i])

    plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.plot(tbase, exact_solution,color='blue', label='esatta')
    plt.plot(tbase, y, color='red', label='mid-point')
    plt.legend(loc='lower left')
    plt.xlabel('t - h='+str(h))
    plt.ylabel('y')
    plt.savefig('./figs/03-midpoint-example-MIN=%s-MAX=%s-h=%s.eps' % (MIN, MAX, h), dpi=SAVE_FIG_DPI)

plot(0, 2.5, 0.02)
plot(0, 2.5, 0.01)
plot(0, 4, 0.001)
plot(0,16,0.001)
plot(0,5,0.0001)
#plt.show()