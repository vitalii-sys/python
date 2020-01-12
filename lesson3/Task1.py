i1 = float(input('Input first digit: '))
i2 = float(input('Input second digit: '))


def division(a1, a2):
    if a2 == 0:
        print('Division by zero error!!!')
    else:
        a = a1 / a2
        print(round(a, 3))


division(i1, i2)
