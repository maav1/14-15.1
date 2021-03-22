def nok(number_nok):
    for num in range(2, number_nok+1):
        if number_nok % num > 0:
            continue
        else:
            return num


number = int(input('Введите число для которого надо найди НОК: '))
print('Наименьший делитель, отличный от единицы:', nok(number))
