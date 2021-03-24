

one_year = int(input('Введите первый год: '))
two_year = int(input('Введите второй год: '))
for digit in range(one_year, two_year):
    one_digit = digit // 1000
    two_digit = (digit // 100) % 10
    three_digit = (digit // 10) % 10
    four_digit = digit % 10
    if ((four_digit == three_digit and four_digit == two_digit) or
        (four_digit == three_digit and four_digit == one_digit) or
        (four_digit == two_digit and four_digit == one_digit) or
        (three_digit == two_digit and three_digit == one_digit)):
        print(digit)


# зачет!
