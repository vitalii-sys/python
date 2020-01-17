from itertools import count, cycle


for el in count(int(input('Введите стартовое число '))):
    if el > 10:
        break
    else:
        print(el)


my_list = [True, 'ABC', 123, None]
how = int(input('How many iterations? '))
n = 0
for el in cycle(my_list):
    if n >= how:
        break
    else:
        print(el)
        n += 1
