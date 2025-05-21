import numpy as np
import matplotlib.pyplot as plt
import math as m

def sgn(x):
    return np.sign(x) if x !=0 else 0

def akc(vx, vy, D, m, g = 9.81):
    ax = -(D/m)*vx**2 * sgn(vx)
    ay = -g-(D/m)*vy**2 * sgn(vy)
    return ax, ay

def Eksplicitna_step(x, y, vx, vy, dt, D, m, g = 9.81):
    ax, ay = akc(vx, vy, D, m)
    vx_novi = vx + ax*dt
    vy_novi = vy + ay*dt
    x_novi = x + vx*dt
    y_novi = y + vy*dt
    return x_novi, y_novi, vx_novi, vy_novi

def RK4_step(x, y, vx, vy, dt, D, m, g = 9.81):
    k1x, k1y = akc(vx, vy, D, m, g)
    l1x = vx
    l1y = vy
    vx2 = vx + 0.5 * dt * k1x
    vy2 = vy + 0.5 * dt * k1y
    k2x, k2y = akc(vx2, vy2, D, m, g)

    l2x = vx + 0.5 * dt * k2x
    l2y = vy + 0.5 * dt * k2y
    vx3 = vx + 0.5 * dt * k2x
    vy3 = vy + 0.5 * dt * k2y
    k3x, k3y = akc(vx3, vy3, D, m, g)

    l3x = vx + 0.5 * dt * k3x
    l3y = vy + 0.5 * dt * k3y
    vx4 = vx + dt * k3x
    vy4 = vy + dt * k3y
    k4x, k4y = akc(vx4, vy4, D, m, g)

    l4x = vx + dt * k4x
    l4y = vy + dt * k4y
    
    vx_novi = vx + (dt/6) * (k1x + 2*k2x + 2*k3x + k4x)
    vy_novi = vy + (dt/6) * (k1y + 2*k2y + 2*k3y + k4y)

    x_novi = x + (dt/6) * (l1x + 2*l2x + 2*l3x + l4x)
    y_novi = y + (dt/6) * (l1y + 2*l2y + 2*l3y + l4y)

    return vx_novi, vy_novi, x_novi, y_novi

x0 = 0
y0 = 0

alfa = 30
V0 = 5
V0x = V0*m.cos(np.radians(alfa))
V0y = V0*m.sin(np.radians(alfa))
m = 2

ro = 1.23
A = 0.015
C = 1.05
D = ro*A*C/2

dt = 0.1

x_eksp = [x0]
y_eksp = [y0]
vx_eksp = [V0x]
vy_eksp = [V0y]
t = 0

x_RK4 = [x0]
y_RK4 = [y0]
vx_RK4 = [V0x]
vy_RK4 = [V0y]

while y_eksp[-1]>=0 or vy_eksp[-1]>=0:
    X, Y, VX, VY = Eksplicitna_step(x_eksp[-1], y_eksp[-1], vx_eksp[-1], vy_eksp[-1], dt, D, m)
    x_eksp.append(X)
    y_eksp.append(Y)
    vx_eksp.append(VX)
    vy_eksp.append(VY)
    t += dt

    X, Y, VX, VY = RK4_step(x_RK4[-1], y_RK4[-1], vx_RK4[-1], vy_RK4[-1], dt, D, m)
    x_RK4.append(X)
    y_RK4.append(Y)
    vx_RK4.append(VX)
    vy_RK4.append(VY)
    t += dt

plt.figure(figsize=(10, 8))
plt.plot(x_eksp, y_eksp, 'r')
plt.plot(x_RK4, y_RK4, 'g')
plt.xlabel('Udaljenost [m]')
plt.ylabel('Visina [m]')
plt.show()