

def finding_sum_digits(number_summa):
    summa_digit_inner = 0
    for digit in number_summa:
        summa_digit_inner += int(digit)
    return summa_digit_inner  # Возвращает сумму


def quantity_digit(number_one, summa_digit_inner):
    counter = 0
    while number_one != 0:
        counter += 1
        number_one = number_one // 10
    # TODO почему добавили _func
    difference_func = summa_digit_inner - counter
    return counter, difference_func  # Возвращает количество и разность


number = input('Введите число: ')
print('Сумма цифр:', finding_sum_digits(number))
summa_digit = finding_sum_digits(number)
count_number, difference = quantity_digit(int(number), summa_digit)
print('Количество цифр:', count_number)
print('Разность суммы и кол-ва цифр:', difference)

# зачет!

