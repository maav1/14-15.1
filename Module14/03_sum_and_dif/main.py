# TODO здесь писать код

def finding_sum_digits(number):
    summ_digit = 0
    for digit in range(number):
        summ_digit += int(digit)
    return summ_digit

def quantity_digit(number):
    count = 0
    while number > 1:
        count += 1
        number = number // 10
    diff = finding_sum_digits(number) - count
    return count,diff

number = input('Введите число: ')
print('Сумма цифр:',finding_sum_digits(number))
print('Колличество цифр:',quantity_digit(int(number)))
print('Разность суммы и кол-ва цифр:',quantity_digit(int(number)))