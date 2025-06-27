import math
import matplotlib.pyplot as plt

def tocka(x, y, x0, y0, r):
    #Izračun udaljenosti točke od središta kružnice
    udaljenost = math.sqrt((x - x0)**2 + (y - y0)**2)
    
    #Određivanje položaja točke
    if udaljenost == r:
        print('Točka je na kružnici.')
    elif udaljenost < r:
        print('Točka je unutar kružnice.')
    else:
        print('Točka je izvan kružnice.')
    
    print(f'Udaljenost od kružnice je {abs(udaljenost - r):.2f}')

    #Crtanje kružnice i točke
    fig, ax = plt.subplots()
    ax.add_patch(plt.Circle((x0, y0), r, fill = False, color = 'black'))
    ax.plot(x, y, 'ro')
    ax.set_aspect('equal')
    ax.set_xlim(x0 - r - 1, x0 + r + 1)
    ax.set_ylim(y0 - r - 1, y0 + r + 1)
    plt.grid(True)
    
    #Korisnički izbor za prikaz ili spremanje slike
    izbor = input('Želite li prikazati sliku (p) ili je spremiti (s)?').lower()
    if izbor == 's':
        ime = input('Unesite naziv datoteke (bez ekstenzije):')
        plt.savefig(f"{ime}.png")
        print(f'Slika je spremljena kao {ime}.png')
    else:
        plt.show()

#Točka na kružnici
#tocka(3, 4, 0, 0, 5)

#Točka unutar kružnice
#tocka(2, 2, 0, 0, 5)

#Točka izvan kružnice
#tocka(5, 5, 0, 0, 5)