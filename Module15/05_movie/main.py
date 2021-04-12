from pprint import pprint

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
print('Выберите из списка понравившиеся ')
pprint(films)

films_like = []
while True:
    like_film = input('Введите название фильма (введите "стоп" для выхода): ')

    if like_film in films:
        films_like.append(like_film)
        print('Фильм', like_film, 'добавлен в избранное.\n')
    elif like_film == "стоп":
        break
    else:
        print('В списке нет такого фильма.')
        continue
print("Список понравившихся фильмов:")
pprint(films_like)
