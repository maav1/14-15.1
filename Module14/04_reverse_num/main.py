
def enter_data():
    enter_number1 = input('Введите первое число: ')
    enter_number2 = input('Введите второе число: ')
    return enter_number1 + '. ' + enter_number2 + '. '


def number_revers(number_for_revers):
    num_revers = number_for_revers[::-1]
    return num_revers


point = ['.']
number1 = enter_data()
probel = [' ']
total_num = number = []
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
new_num1 = new_num2 = ''
for i in total_num:
    if i == ' ':
        flag = 1

    if not flag:
        new_num1 += i
    else:
        new_num2 += i
first_number_output = float(new_num1)
second_number_output = float(new_num2)
summ_output = round(first_number_output + second_number_output, 3)
print('\nПервое число наоборот:', first_number_output, '\nВторое число наоборот:', second_number_output,
      '\n\nИх сумма:', summ_output)
