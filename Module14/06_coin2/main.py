def calculating(x_func, y_func, radius_func):
    if x_func ** 2 + y_func ** 2 <= radius_func ** 2:
        print('Монетка рядом.')
    else:
        print('Монетка далеко.')


print('Введите координаты монетки:')
money_x = float(input('X: '))
money_y = float(input('Y: '))
radius_around = int(input('Введите радиус: '))
calculating(money_x, money_y, radius_around)

# зачет!

