try:
    with open('file4task5.txt', 'w+') as f:
        digits = input('Input some digits separated by space:\n')
        f.writelines(digits)
        digits2 = digits.split()
        print(sum(map(int, digits2)))
except ValueError:
    print('ValueError!')
