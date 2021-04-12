
row_elements = []
number_elements = int(input('Введите количество элементов списка: '))
for i in range(number_elements):
    row_elements.append(int(input(f'Введите элемент {i + 1}: ')))
print('Список элементов:', row_elements, '\n')
row_elements.sort()
print('Отсортированный список:', row_elements)
