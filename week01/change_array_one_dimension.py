import numpy as np

a = np.zeros((2, 3))
print(a)

b = a.reshape((6,))
print(b)

c = a.reshape(-1)

d = np.ravel(a)
print(d)