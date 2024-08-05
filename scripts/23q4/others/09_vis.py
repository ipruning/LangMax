import matplotlib.pyplot as plt
import numpy as np

N = int(1e4)
D = 2
X = np.random.randn(N, D)
plt.plot(X[:, 0], X[:, 1], ".")
plt.axis("square")
plt.show()
