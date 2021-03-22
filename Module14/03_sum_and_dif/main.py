

def finding_sum_digits(number_summ):
    summ_digit_func = 0
    for digit in number_summ:
        summ_digit_func += int(digit)
    return summ_digit_func  # Возвращает сумму


def quantity_digit(number_one, summ_digit_func):
    count_def = 0
    while number_one != 0:
        count_def += 1
        number_one = number_one // 10
    diff_func = summ_digit_func - count_def
    return count_def, diff_func  # Возвращает количество и разность


number = input('Введите число: ')
print('Сумма цифр:', finding_sum_digits(number))
summ_digit = finding_sum_digits(number)
count, diff = quantity_digit(int(number), summ_digit)
print('Количество цифр:', count)
print('Разность суммы и кол-ва цифр:', diff)
