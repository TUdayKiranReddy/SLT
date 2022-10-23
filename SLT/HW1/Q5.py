import numpy as np
import matplotlib.pyplot as plt

def X(n):
    return np.power(-1, n)*np.random.uniform()/n


N = np.arange(1, 10000, 2)

plt.figure()
plt.title(r'$X_n$')
plt.scatter(N, [X(n) for n in N], marker='.', label='ODD')
plt.scatter(N+1, [X(n) for n in N+1], marker='.', label='EVEN')
plt.ylim([-1e-2, 1e-2])
plt.ylabel('Amplitude')
plt.xlabel('N')
plt.legend()
plt.savefig('Q5_plot.jpeg')
plt.show()
