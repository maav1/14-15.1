
def enter_number():
    print("Введите первую точку")
    enter_x1 = float(input('X: '))
    enter_y1 = float(input('Y: '))
    print("\nВведите вторую точку")
    enter_x2 = float(input('X: '))
    enter_y2 = float(input('Y: '))
    return enter_x1, enter_x2, enter_y1, enter_y2


coordinate_x1, coordinate_x2, coordinate_y1, coordinate_y2 = enter_number()
x_diff = coordinate_x1 - coordinate_x2
y_diff = coordinate_y1 - coordinate_y2
if x_diff != 0 and y_diff != 0:
    k = y_diff / x_diff
    b = coordinate_y2 - k * coordinate_x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)
elif x_diff == 0 and y_diff != 0:
    print('При данных значениях,  функция принимает вид: х = b, где b =', coordinate_x1,
          '\nа график функции параллелен оси ОY и смещён по оси ОХ на', coordinate_x1)
elif x_diff != 0 and y_diff == 0:
    print('При данных значениях, функция принимает вид: у = b, где b =', coordinate_y1,
          '\nа график функции параллелен оси ОX и смещён по оси OY на', coordinate_y1)


