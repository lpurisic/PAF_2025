import matplotlib.pyplot as plt
import numpy as np

def jednadzba_pravca(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = k * (-x1) + y1
    print('y = {}x + {}'.format(k, l))

x1 = float(input('Unesite prvu x koordinatu: '))
y1 = float(input('Unesite prvu y koordinatu: '))
x2 = float(input('Unesite drugu x koordinatu: '))
y2 = float(input('Unesite drugu y koordinatu: '))
jednadzba_pravca(x1, y1, x2, y2)

k = (y2 - y1) / (x2 - x1)
l = k * (-x1) + y1
x = np.linspace(x1, x2)
y = k * x + l
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, 'b')

spremanje = input('Želite li graf prikazat u programu ili ga spremit u pdf datoteku? (program/pdf)')
if spremanje == 'program':
    plt.show()
elif spremanje == 'pdf':
    filename = input('Unesi ime za pdf datoteku: ').strip()
    plt.savefig(filename, format='pdf')