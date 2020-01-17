from sys import argv


name, time, salary, bonus = argv
try:
    time = float(time)
    salary = float(salary)
    bonus = float(bonus)
    res = time * salary + bonus
    print(f'Salary is: {res}')
except ValueError:
    print('Not a number')
