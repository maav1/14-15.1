
# from time import sleep
row_elements = []
number_elements = int(input('Введите количество элементов списка: '))
for i in range(number_elements):
    row_elements.append(int(input(f'Введите элемент {i + 1}: ')))
print('Список элементов:', row_elements)
offset = int(input('Введите смещение: '))
for _ in range(offset):
    row_elements.insert(0, row_elements.pop())
print('Новый список: ', row_elements)


'''
Здесь хотел сделать "Бегущую строку", но не работает нормально
while True:
    print(row_elements, end='\r')
    row_elements.insert(0, row_elements.pop())
    print(row_elements, end='\r')
    sleep(1)
'''

# зачет!
