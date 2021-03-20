def calculating(x,y,r):
    if x ** 2 + y ** 2 <= r ** 2:
        print('Монетка рядом.')
    else:
        print('Монетка далеко.')
print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))
calculating(x,y,r)