number_cell = int(input('Введите количество клеток: '))
cell = []
for count in range(number_cell):
  efficiency_cell = int(input(f"Эффективность {count + 1} клетки:"))
  if efficiency_cell < count + 1:
     cell.append(str(efficiency_cell))
print('Не подходящие значения:', *cell)


# TODO недочеты в оформлении
