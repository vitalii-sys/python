with open('text4task2.txt') as f:
    c = f.read()
    print(f'Content of file:\n{c}')
with open('text4task2.txt') as f:
    cl = f.readlines()
    print(f'Quantity of strings: {len(cl)}')
with open('text4task2.txt') as f:
    for i in range(len(cl)):
        cs = f.readline()
        cs = cs.split()
        print(f'Quantity of words in {i + 1} string is {len(cs)}')
