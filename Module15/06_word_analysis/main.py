count = 0
new_word = []
word = list(input('Введите слово: '))
for letter in word:
    if word.count(letter) > 1 and letter not in new_word:
        count += word.count(letter)
    new_word.append(letter)
print('Уникальных букв:', len(word) - count)

# зачет!
