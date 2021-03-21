
def enter():
    print("Введите первую точку")
    x1 = float(input('X: '))
    y1 = float(input('Y: '))
    print("\nВведите вторую точку")
    x2 = float(input('X: '))
    y2 = float(input('Y: '))
    return x1,x2,y1,y2

x1,x2,y1,y2 = enter()


x_diff = x1 - x2
y_diff = y1 - y2
if x_diff != 0 and y_diff != 0:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)
elif x_diff == 0 and y_diff != 0:
    print('При данных значениях,  функция принимает вид: х = b, где b =', x1, '\nа график функции параллелен оси ОY и смещён по оси ОХ на',x1)
elif x_diff != 0 and y_diff == 0:
    print('При данных значениях, функция принимает вид: у = b, где b =', y1, '\nа график функции параллелен оси ОX и смещён по оси OY на',y1)



