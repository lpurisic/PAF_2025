import particle as pr
import math

cestica = pr.Particle(v0 = 25, theta = 45, x0 = 0, y0 = 0)

domet = cestica.range(dt = 1)

print(domet)

cestica.plot_trajectory()