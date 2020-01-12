def my_func(a, b, c):
    if min(a, b, c) == a:
        print(b + c)
    elif min(a, b, c) == b:
        print(a + c)
    elif min(a, b, c) == c:
        print(a + b)


my_func(4, 2, 0)
