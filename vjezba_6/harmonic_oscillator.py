import math
import numpy as np

class HarmonicOscillator:
    def __init__(self, m, k, x0, v0):
        self.m = m #kg
        self.k = k #N/m
        self.x0 = x0 #m
        self.v0 = v0 #m/s
        self.omega = np.sqrt(k / m)

    def an_rj(self, t):
        x = self.x0 * np.cos(self.omega * t) + (self.v0 / self.omega) * np.sin(self.omega * t)
        v = -self.x0 * self.omega * np.sin(self.omega * t) + self.v0 * np.cos(self.omega * t)
        a = -self.omega**2 * x
        return x, v, a
    
    def num_rj(self, t_max, dt):
        n = int(t_max / dt) + 1
        t = np.linspace(0, t_max, n)

        x = []
        self.x0.append(x)
        v = []
        self.v0.append(v)
        a = []
        a = -self.k / self.m * x
        a.append(a)

        for i in range(1, n):
            a[i-1] = -self.k / self.m * x[i-1]
            v[i] = v[i-1] + a[i-1] * dt
            x[i] = x[i-1] + v[i-1] * dt
            a[i] = -self.k / self.m * x[i]

        return t, x, v, a
        