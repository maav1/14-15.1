cards = []
number_videocards = int(input('Количество видеокарт: '))
print('Введите коды видеокарт:')
for card in range(number_videocards):
    # TODO инпуты всегда пишем отдельной строкой не нужно из вставлять в списки
    cards.append(int(input(f'Видеокарта {card + 1}:')))
print('Старый список видеокарт:')
print(cards)
# TODO что за некий element ?
for element in cards:
    if int(element) == max(cards):
        cards.remove(element)
print('Новый список видеокарт:')
print(cards)
