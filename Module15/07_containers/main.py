
container_quantity = int(input('Количество контейнеров: '))
lst_containers = []
text_all_containers = ['Введите вес контейнера (не более 200): ']
text_new_container = ['Введите вес нового контейнера: ']
count = 0


def func_input(text_exit):
    try:
        temp_number = int(input(text_exit))
    except ValueError:
        print('Ошибка ввода. Повторите ещё раз.')
        return 0

    if temp_number > 200:
        print('Ошибка ввода. Повторите ещё раз.')
        return 0
    else:
        return temp_number


while container_quantity > 0:
    number_container = func_input(text_all_containers)
    if number_container != 0:
        lst_containers.append(number_container)
        container_quantity -= 1
    else:
        continue

lst_containers.sort(reverse=True)
print('\nНовый список, сортированный по-убыванию:', lst_containers)
print()
new_container = func_input(text_new_container)
for j in lst_containers:
    count += 1
    if count == len(lst_containers):
        lst_containers.append(new_container)
        count += 1
        break
    elif new_container >= j:
        lst_containers.insert(count - 1, new_container)
        break


print('\nНомер, куда встанет новый контейнер: ', count)
print('\nСписок с новым контейнером:', lst_containers)
