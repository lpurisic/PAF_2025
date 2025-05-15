import numpy as np
import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator as osc

masa = 1 #kg
k = 10 #N/m
x0 = 1 #m
v0 = 0 #m/s
t_max = 10 #s

osc(masa, k, x0, v0)

dt_vrijednosti = [0.1, 0.05, 0.01]

for dt in dt_vrijednosti:
    t, x_num, v_num, a_num = osc.num_rj(t_max, dt)
    x_an, v_an, a_an = osc.an_rj(t)

    plt.figure(figsize=(8, 8))

    #x - t
    plt.plot(t, x_an)
    plt.plot(t, x_num,)
    plt.xlabel('t [s]')
    plt.ylabel('x(t) [m]')
    plt.legend()

    #v - t
    plt.plot(t, v_an)
    plt.plot(t, v_num)
    plt.xlabel('t [s]')
    plt.ylabel('v(t) [m/s]')

    #a - t
    plt.plot(t, a_an)
    plt.plot(t, a_num)
    plt.ylabel('a(t) [m/s^2]')
    plt.xlabel('t [s]')
    
    plt.show()