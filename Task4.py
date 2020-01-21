dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('file4task4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_list.append(dic[i[0]] + ' ' + i[1])
    print(new_list)


with open('file4task4new.txt', 'w') as f2:
    f2.writelines(new_list)
