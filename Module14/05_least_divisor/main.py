def nok(number_nok):
    for number_in_lst in range(2, number_nok+1):
        if number_nok % number_in_lst > 0:
            continue
        else:
            return number_in_lst


number = int(input('Введите число для которого надо найди НОК: '))
print('Наименьший делитель, отличный от единицы:', nok(number))

# зачет!

