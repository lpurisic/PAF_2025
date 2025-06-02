import numpy as np
import matplotlib.pyplot as plt
import math as m

def akc(V, q, m, E, B):
    vx = V[0]
    vy = V[1]
    vz = V[2]
    Ex = E[0]
    Ey = E[1]
    Ez = E[2]
    Bx = B[0]
    By = B[1]
    Bz = B[2]

    ax = (q/m) * (Ex + vy * Bz - vz * By)
    ay = (q/m) * (Ey - (vx * Bz - vz * Bx))
    az = (q/m) * (Ez + vx * By - vy * Bx)

    return ax, ay, az

def Eksplicitna_step(x, y, z, V, dt, q, m, E, B):
    vx = V[0]
    vy = V[1]
    vz = V[2]

    ax, ay, az = akc(V, q, m, E, B)
    vx_novi = vx + ax * dt
    vy_novi = vy + ay * dt
    vz_novi = vz + az * dt

    x_novi = x + vx * dt
    y_novi = y + vy * dt
    z_novi = z + vz * dt

    return x_novi, y_novi, z_novi, vx_novi, vy_novi, vz_novi

def RK4_step(x, y, z, V, dt, q, m, E, B):
    vx = V[0]
    vy = V[1]
    vz = V[2]

    k1x, k1y, k1z = akc(V, q, m, E, B)
    l1x = vx
    l1y = vy
    l1z = vz
    vx2 = vx + 0.5 * dt * k1x
    vy2 = vy + 0.5 * dt * k1y
    vz2 = vz + 0.5 * dt * k1z
    V2 = [vx2, vy2, vz2]
    k2x, k2y, k2z = akc(V2, q, m, E, B)

    l2x = vx + 0.5 * dt * k2x
    l2y = vy + 0.5 * dt * k2y
    l2z = vz + 0.5 * dt * k2z
    vx3 = vx + 0.5 * dt * k2x
    vy3 = vy + 0.5 * dt * k2y
    vz3 = vz + 0.5 * dt * k2z
    V3 = [vx3, vy3, vz3]
    k3x, k3y, k3z = akc(V3, q, m, E, B)

    l3x = vx + 0.5 * dt * k3x
    l3y = vy + 0.5 * dt * k3y
    l3z = vz + 0.5 * dt * k3z
    vx4 = vx + dt * k3x
    vy4 = vy + dt * k3y
    vz4 = vz + dt * k3z
    V4 = [vx4, vy4, vz4]
    k4x, k4y, k4z = akc(V4, q, m, E, B)
    l4x = vx + dt * k4x
    l4y = vy + dt * k4y
    l4z = vz + dt * k4z

    vx_novi = vx + (dt/6) * (k1x + 2 * k2x + 2 * k3x + k4x)
    vy_novi = vy + (dt/6) * (k1y + 2 * k2y + 2 * k3y + k4y)
    vz_novi = vz + (dt/6) * (k1z + 2 * k2z + 2 * k3z + k4z)

    x_novi = x + (dt/6) * (l1x + 2 * l2x + 2 * l3x + l4x)
    y_novi = y + (dt/6) * (l1y + 2 * l2y + 2 * l3y + l4y)
    z_novi = z + (dt/6) * (l1z + 2 * l2z + 2 * l3z + l4z)

    return x_novi, y_novi, z_novi, vx_novi, vy_novi, vz_novi

x0 = 0
y0 = 0
z0 = 0

V0 = [18, 15, 12]
E = [0, 0, 0]
B = [0, 0, 1]

q = 1
m = 1

x_eksp = [x0]
y_eksp = [y0]
z_eksp = [z0]
vx_eksp = [V0[0]]
vy_eksp = [V0[1]]
vz_eksp = [V0[2]]

x_RK4 = [x0]
y_RK4 = [y0]
z_RK4 = [z0]
vx_RK4 = [V0[0]]
vy_RK4 = [V0[1]]
vz_RK4 = [V0[2]]

dt = 0.01
vrijeme = 10 #s
t = np.arange(0, vrijeme, dt)

for i in range(len(t)):
    X, Y, Z, VX, VY, VZ = Eksplicitna_step(x_eksp[-1], y_eksp[-1], z_eksp[-1], V = [vx_eksp[-1], vy_eksp[-1], vz_eksp[-1]], dt = dt, q = q, m = m, E = E, B = B)
    x_eksp.append(X)
    y_eksp.append(Y)
    z_eksp.append(Z)
    vx_eksp.append(VX)
    vy_eksp.append(VY)
    vz_eksp.append(VZ)

    X, Y, Z, VX, VY, VZ = RK4_step(x_RK4[-1], y_RK4[-1], z_RK4[-1], V = [vx_RK4[-1], vy_RK4[-1], vz_RK4[-1]], dt = dt, q = q, m = m, E = E, B = B)
    x_RK4.append(X)
    y_RK4.append(Y)
    z_RK4.append(Z)
    vx_RK4.append(VX)
    vy_RK4.append(VY)
    vz_RK4.append(VZ)


plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})
ax.plot(x_eksp, y_eksp, z_eksp, 'r')
ax.plot(x_RK4, y_RK4, z_RK4, 'b')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()