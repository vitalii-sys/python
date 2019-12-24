my_list = []
num = int(input(f'Введите количество элементов списка: '))
for i in range(num):
    new_el = input(f'Введите новый элемент списка: ')
    my_list.append(new_el)

print(my_list)

for a in range(1, num, 2):
    my_list[a-1], my_list[a] = my_list[a], my_list[a-1]

print(my_list)