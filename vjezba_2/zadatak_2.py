

import numpy as np
import matplotlib.pyplot as plt


v0 = int(input("Unesite početnu brzinu: "))
theta= int(input("Unesite kut: "))
theta_rad = np.radians(theta)


g = 9.81         
t_max = 10        
dt = 0.01         
n = int(t_max / dt) + 1


t = np.linspace(0, t_max, n)
x = np.zeros(n)
y = np.zeros(n)
vx = np.zeros(n)
vy = np.zeros(n)
ax = np.zeros(n)
ay = np.zeros(n)

vx[0] = v0 * np.cos(theta_rad)
vy[0] = v0 * np.sin(theta_rad)
ax[:] = 0
ay[:] = -g

for i in range(1, n):
    vx[i] = vx[i-1] + ax[i-1] * dt
    vy[i] = vy[i-1] + ay[i-1] * dt
    x[i] = x[i-1] + vx[i-1] * dt
    y[i] = y[i-1] + vy[i-1] * dt

    if y[i] < 0:
        x = x[:i+1]
        y = y[:i+1]
        t = t[:i+1]
        break


plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.plot(x, y, color='blue')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("x - y graf (Putanja projektila)")


plt.subplot(3, 1, 2)
plt.plot(t, x, color='green')
plt.xlabel("Vrijeme (s)")
plt.ylabel("x (m)")
plt.title("x - t graf")


plt.subplot(3, 1, 3)
plt.plot(t, y, color='red')
plt.xlabel("Vrijeme (s)")
plt.ylabel("y (m)")
plt.title("y - t graf")


plt.tight_layout()
plt.show()
