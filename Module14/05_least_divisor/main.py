def nok(number):
    for i in range(2,number+1):
        if number % i > 0:
            continue
        else:
            break
    # TODO i сейчас вне цикла и не может вернуться
    return i

number = int(input('Введите число для которого надо найди НОК: '))
print('Наименьший делитель, отличный от единицы:',nok(number))

# TODO применяем рекомендации данные в 01
# TODO нейминг переменных пишем все переменные развернуто
