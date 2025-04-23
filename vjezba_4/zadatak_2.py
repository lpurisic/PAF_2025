import numpy as np
import matplotlib.pyplot as plt

v0 = 10 #pocetna brzina u m/s
#theta = 60 stupnjeva
theta = np.pi / 3 #rad
g = 9.81 #m/s^2

v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

R_an = (v0**2 * np.sin(2 * theta)) / g
delta_t = np.linspace(0.001, 1, 100)
rel_err = []

for dt in delta_t:
    x = 0
    y = 0
    vx = v0x
    vy = v0y
    t = 0

    while y >= 0:
        x += vx * dt
        y += vy * dt
        vy -= g * dt
        t += dt

    R_num = x
    rel_error = abs(R_num - R_an) / R_an
    rel_err.append(rel_error)

plt.figure(figsize=(8, 5))
plt.plot(delta_t, rel_err)
plt.xlabel('∆t [s]')
plt.ylabel('Relativna pogreška [%]')
plt.show()