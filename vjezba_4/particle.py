import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0 = 0, y0 = 0):
        self.v0 = v0
        self.theta = math.radians(theta)
        self.x0 = x0
        self.y0 = y0

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)
        self.t = 0
        self.x_tocke = [self.x]
        self.y_tocke = [self.y]

    def __move(self, dt):
        g = 9.81
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy -= g * dt
        self.x_tocke.append(self.x)
        self.y_tocke.append(self.y)

    def range(self, dt = 1):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self):
        plt.plot(self.x_tocke, self.y_tocke)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()