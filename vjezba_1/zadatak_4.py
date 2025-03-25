def jednadzba_pravca(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = k * (-x1) + y1
    print('y = {}x + {}'.format(k, l))

x1 = float(input('Unesite prvu x koordinatu: '))
y1 = float(input('Unesite prvu y koordinatu: '))
x2 = float(input('Unesite drugu x koordinatu: '))
y2 = float(input('Unesite drugu y koordinatu: '))
jednadzba_pravca(x1, y1, x2, y2)