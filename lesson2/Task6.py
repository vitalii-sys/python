lst = []
dic = {}
step = 1
d = {"название": [], "цена": [], "количество": [], "ед": []}

product_quantity = int(input('Введите общее количество наименований товаров: '))
while product_quantity >= step:
    n = input('Введите название товара: ')
    p = int(input('Введите цену товара: '))
    q = int(input('Введите количество вашего товара: '))
    u = input('Введите единицу измерения товара: ')
    dic = (step, {"название": n, "цена": p, "количество": q, "ед": u})
    lst.append(dic)
    step += 1
    d["название"].append(n)
    d["цена"].append(p)
    d["количество"].append(q)
    d["ед"].append(u)
    d["ед"] = list(set(d["ед"]))
print('[')
for i in lst:
    print(i)
print(']')
print('{')
for key, value in d.items():
    print(key, value)
print('}')