def nok(number_nok):
    for number_temp in range(2, number_nok+1):
        if number_nok % number_temp > 0:
            continue
        else:
            return number_temp


number = int(input('Введите число для которого надо найди НОК: '))
print('Наименьший делитель, отличный от единицы:', nok(number))

# зачет!

