import numpy as np
import matplotlib.pyplot as plt

G = 6.67408e-11 #[Nm^2/kg^2]
ms = 1.989e30 #[kg]
mz = 5.9742e24 #[kg]
au = 1.496e11 #[m]
v0 = 29783 #[m/s]
godina_d = 365.242 #dani
godina = 31556908.8 #[s]

dt = 3600 #[s]
koraci = int(godina / dt)

x_sunce, y_sunce = 0, 0
x_zemlja, y_zemlja = au, 0

vx_sunce, vy_sunce = 0, 0
vx_zemlja, vy_zemlja = 0, v0

x_z = []
y_z = []

x, y = x_zemlja, y_zemlja
vx, vy = vx_zemlja, vy_zemlja

for i in range(koraci):
    dx = x - x_sunce
    dy = y - y_sunce
    r = np.sqrt(dx**2 + dy**2)

    F = -G * ms / r**3
    ax = F * dx
    ay = F * dy

    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt

    x_z.append(x)
    y_z.append(y)

plt.figure(figsize = (8, 8))
plt.plot(0, 0, 'yo', label = 'Sunce')
plt.plot(x_z, y_z, 'b-', label = 'Zemlja')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend()
plt.show()