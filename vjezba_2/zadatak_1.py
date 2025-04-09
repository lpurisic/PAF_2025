
import numpy as np
import matplotlib.pyplot as plt

F = int(input("Unesite silu: "))
m =int(input("Unesite masu:  "))


t_max = 10        
dt = 0.1           
n = int(t_max / dt) + 1
t = np.linspace(0, t_max, n)
a = np.zeros(n)
v = np.zeros(n)
x = np.zeros(n)


a= F / m


for i in range(1, n):
    v[i] = v[i-1] + a[i-1] * dt
    x[i] = x[i-1] + v[i-1] * dt

plt.figure(figsize=(12, 8))


plt.subplot(3, 1, 1)
plt.plot(t, x, label='x(t)', color='blue')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Položaj (m)')
plt.title('x - t graf')


plt.subplot(3, 1, 2)
plt.plot(t, v, label='v(t)', color='green')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Brzina (m/s)')
plt.title('v - t graf')

plt.subplot(3, 1, 3)
plt.plot(t, a, label='a(t)', color='red')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Ubrzanje (m/s²)')
plt.title('a - t graf')


plt.tight_layout()
plt.show()
