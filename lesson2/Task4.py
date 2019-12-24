string = input('Введите несколько слов через пробел: ')
words = string.split()

for i, word in enumerate(words, start=1):
    print(i, word[:10])
