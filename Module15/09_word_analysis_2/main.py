
flag = 0
word = input('Введите слово: ')
for i in range(0,(len(word) // 2)):
    if word[i] != word[-i - 1]:
        flag = 1
        break
if flag:
    print('Слово не является палиндромом.')
else:
    print('Слово является палиндромом.')

# зачет!
