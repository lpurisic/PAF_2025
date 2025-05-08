import math
import numpy as np
import matplotlib.pyplot as plt

class Calculus:
    def __init__(self, f, x, epsilon):
        self.f = f
        self.x = x
        self.epsilon = epsilon

    def derivacija(self, f, x, epsilon, metoda = 'three-step'):
        if metoda == 'two-step':
            return (f(x + epsilon) - f(x) / epsilon)
        else:
            (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

    def numericka_derivacija(f, donja, gornja, epsilon=1e-5, metoda = 'three-step'):
        tocke = np.linspace(donja, gornja, 100)
        derivacije = []

        for x in tocke:
            der = Calculus.derivacija(f, x, epsilon, metoda)
            derivacije.append((x, der))

        return derivacije

    def pravokutna_aproksimacija(f, donja, gornja, n):
        h = (gornja - donja) / n
        a = np.linspace(donja, gornja - h, n)
        b = np.linspace(donja + h, gornja, n)

        DS = np.sum(f(a)) * h
        GS = np.sum(f(b)) * h

        return DS, GS
    
    def trapezoidno_pravilo(f, donja, gornja, n):
        dx = (gornja-donja)/n
        suma = 0.5 * (f(donja) + f(gornja))
    
        for i in range(1, n):
            suma += f(donja+i*dx)
        return suma*dx
