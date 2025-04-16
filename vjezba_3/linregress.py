import matplotlib.pyplot as plt
import numpy as np
import math

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336]) #Nm
fi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]) #rad
#M = D_t * fi
#D_t = M / fi
#y = ax + b, b = 0
#D_t = a
#x = fi
#y = M
n = 6

fi2 = (x**2 for x in fi)
x = sum(fi) / len(fi)
x2 = sum(fi2) / len(fi)

M2 = (y**2 for y in M)
y = sum(M) / len(M)
y2 = sum(M2) / len(M)

xy = M * fi
ar_sr_xy = sum(xy) / len(xy)

a = ar_sr_xy / x2

sigma = math.sqrt((1 / n) * ((y2 / x2) - a**2))

plt.figure(figsize=(8, 5))
plt.xlabel('fi [rad]')
plt.ylabel(' M [Nm]')
plt.plot(fi, M, 'r.')
plt.plot(fi, a * fi)
plt.show()