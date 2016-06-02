from env import *
PLOT_MARKER = plot_marker_generator()

def get_S_Sp(L, p):
    size = L.shape[0]
    f = L.sum(axis=0)
    fplus = np.copy(f)
    fplus[fplus > 0] **= -1

    F = np.diag(fplus)

    H = np.dot(L, F)

    v = np.ones((size, 1)) / size
    d = 1 - f * fplus
    d = d.reshape((size, 1))
    # in this case wen can easily correct for approximation errors
    d[d > 0.5] = 1
    d[d < 0.5] = 0

    S = H + v.dot(d.transpose())
    Sp = p * S + (1 - p) * v.dot(np.ones((1, size)))

    return S, Sp


def exact_solution(S, p):
    n = S.shape[0]
    k = (1 - p) / n
    M = np.linalg.inv((np.identity(n) - p * S))
    sol = k * M.dot(np.ones(n))
    return sol.reshape((n, 1))


def pagerank(S, x, maxiters):
    res = [x]
    for i in range(maxiters):
        res.append(S.dot(res[i]))
    return res


def generate_x_L(size, t = 0.99):
    x = np.ones((size, 1))
    x /= size
    L = np.random.random((size, size))
    L[L >= t] = 1
    L[L < t] = 0
    return x, L


def solve(L, x, p, maxiters=100):
    S, Sp = get_S_Sp(L, p)
    res = pagerank(Sp, x, maxiters)
    return res


def plot_p_comparison():
    fig = plt.figure(figsize=FIG_SIZE_2D, dpi=FIG_DPI_2D)
    plt.grid(**GRID_OPTIONS)
    maxiters = 50
    x, L = generate_x_L(500, 0.99)
    for p in np.arange(0.2,0.99,0.11):
        exact = exact_solution(get_S_Sp(L,p)[0],p)
        res = solve(L,x,p,maxiters=maxiters)
        errors = [np.sum(np.abs(r - exact)) for r in res]
        plt.plot(range(maxiters+1), errors, '-'+next(PLOT_MARKER), label='p = %s' % p)

    plt.yscale('log')
    plt.xlabel('Iterations - $L \in M^{500\\times500}$')
    plt.ylabel(r'$\|\textbf x-\textbf x_k\|_1$')
    plt.legend(loc='upper right')
    plt.savefig('./figs/05-randomsurfer-p.eps', dpi=SAVE_FIG_DPI)

plot_p_comparison()
