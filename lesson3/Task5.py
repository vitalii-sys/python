def my_func():
    f_sum = 0
    x = False
    while not x:
        digits = input('Input numbers for summing or Q for quit - ').split()
        s = 0
        for i in range(len(digits)):
            if digits[i] == 'q' or digits[i] == 'Q':
                x = True
                break
            else:
                s += int(digits[i])
        f_sum += s
        print(f'Your current sum is {f_sum}')
    print(f'Your final sum is {f_sum}')


my_func()
