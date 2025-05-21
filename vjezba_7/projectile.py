import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, alfa, m, k, dt):
        self.v0 = v0
        self.alfa = np.radians(alfa)
        self.m = m
        self.k = k
        self.dt = dt
        self.g = 9.81
        self.ro = 1.23
        self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * np.cos(self.alfa)
        self.vy = self.v0 * np.sin(self.alfa)
        self.trajectory = [(self.x, self.y)]

    def step(self):
        ax = -self.k * self.vx / self.m
        ay = -self.k * self.vy / self.m - self.g

        self.vx += ax * self.dt
        self.vy += ay * self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt

        self.trajectory.append((self.x, self.y))

    def simulacija(self):
        while self.y >= 0:
            self.step()
        return np.array(self.trajectory)
    
    def plot_trajectory(self):
        x1, y1 = zip(*self.trajectory)
        plt.plot(x1, y1)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.legend()
        plt.show()

projectile = Projectile(v0 = 50, alfa = 45, m = 0.145, k = 0.47, dt = 0.01)
projectile.simulacija()
projectile.plot_trajectory()