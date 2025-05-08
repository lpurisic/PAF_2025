import numpy as np
import matplotlib.pyplot as plt
from calculus import Calculus

def kubna_funkcija(x):
    return x**3

def trigonometrijska_funkcija(x):
    return np.sin(x)

def an_kub_der(x):
    return 3 * x**2

def an_trig_der(x):
    return np.cos(x)

donja, gornja = -5, 5
epsilon = 1e-5

num_kub = Calculus.numericka_derivacija(kubna_funkcija, donja, gornja, epsilon, 'three-step')
num_trig = Calculus.numericka_derivacija(trigonometrijska_funkcija, donja, gornja, epsilon, 'three-step')

x_vrijednosti = np.linspace(donja, gornja, 100)
an_kub = an_kub_der(x_vrijednosti)
an_trig = an_trig_der(x_vrijednosti)

plt.figure(figsize=(10, 6))
plt.plot(x_vrijednosti, an_kub, color = 'r')
plt.legend()
plt.plot(x_vrijednosti, an_trig, color = 'b')
plt.legend()
plt.tight_layout()
plt.show()

br_koraka = [10, 100, 500, 1000, 5000, 10000]
num_povrsina = [trapezoidno_pravilo(f, donja, gornja, n) for n in br_koraka]

plt.figure(figsize=(12, 8))
plt.plot(br_koraka, num_povrsina, 'o')
plt.legend()
plt.show()