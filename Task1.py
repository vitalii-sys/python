f = open('file4task1.txt', 'w')
line = input('Введите текст \n')
while line:
    f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break


f.close()
f = open('file4task1.txt', 'r')
c = f.readlines()
print(c)
f.close()
