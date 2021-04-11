import numpy as np
x = np.random.rand(20, 20)
a = x.transpose()
b = np.linalg.inv((np.matmul(a,x)))
theta = np.matmul(b,x.transpose())
y = np.random.random_integers(0, 20, 20)
theta = np.matmul(theta, y)
print(theta)

