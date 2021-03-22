
# TODO параметр point должне использоваться
def enter_data(point):
    number1 = input('Введите первое число: ')
    number2 = input('Введите второе число: ')
    return number1 + '. ' + number2 + '. '


def number_revers(number):
    num_revers = number[::-1]
    return num_revers


point = ['.']
number1 = enter_data(point)
probel = [' ']
total_num =number = []
second_point = 0
n = ''
number_one_revers = []
for symb in number1:
    if symb != '.' and symb != ' ':
        number += symb
    elif symb == '.':
        second_point += 1
        n = number_revers(number)
        if second_point != 2:
            number_one_revers += (n + point)
        else:
            number_one_revers += (n + probel)
            second_point = 0
        number = []
    else:
        total_num = ("".join(number_one_revers))
flag = 0
num1 = num2 = ''
for i in total_num:
    if i == ' ':
        flag = 1

    if not flag:
        num1 += i
    else:
        num2 += i
b1 = float(num1)
c1 = float(num2)
summ = round(b1 + c1,3)
print('\nПервое число наоборот:',b1,'\nВторое число наоборот:',c1,'\n\nИх сумма:',summ)

# TODO применяем рекомендации данные в 01
# TODO нейминг переменных пишем все переменные развернуто
