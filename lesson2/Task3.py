# list
num = int(input('Введите номер месяца: '))
months = ['', 'Winter', 'Winter',
          'Spring', 'Spring', 'Spring',
          'Summer', 'Summer', 'Summer',
          'Autumn', 'Autumn', 'Autumn',
          'Winter']
print(months[num])

# dict
months_dict = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5],
               'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
for i, mon in months_dict.items():
    if num in mon:
        print(i)
        


