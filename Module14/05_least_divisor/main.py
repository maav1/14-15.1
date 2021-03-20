def nok(number):
    for i in range(2,number+1):
        if number % i > 0:
            continue
        else:
            break
    return i
number = int(input('Введите число для которого надо найди НОК: '))
print('Наименьший делитель, отличный от единицы:',nok(number))