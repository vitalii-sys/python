chislo = int(input('Введите целое положительное число: '))

maximal = chislo % 10
chislo = chislo // 10

while chislo > 0:
    if chislo % 10 > maximal:
        maximal = chislo % 10
    chislo = chislo // 10

print(f'Наибольшая цифра в числе: {maximal}')
