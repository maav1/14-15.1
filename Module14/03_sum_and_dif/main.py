# TODO здесь писать код

def finding_sum_digits(number):
    summ_digit = 0
    for digit in number:
        summ_digit += int(digit)
    return summ_digit #Возвращает сумму


def quantity_digit(number,summ_digit):
    count = 0
    while number != 0:
        count += 1
        number = number // 10
    diff = summ_digit - count
    return count,diff #Возвращает количество и разность

number = input('Введите число: ')
print('Сумма цифр:',finding_sum_digits(number))
summ_digit = finding_sum_digits(number)
count,diff = quantity_digit(int(number),summ_digit)
print('Колличество цифр:',count)
print('Разность суммы и кол-ва цифр:',diff)
