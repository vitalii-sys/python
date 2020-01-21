with open('file4task3.txt', 'r') as f:
    sal = []
    low = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            low.append(i[0])
            sal.append(i[1])
print(f'Salary less then 20.000: {low}\nAverage salary: {sum(map(float, sal)) / len(sal):.2f}')
