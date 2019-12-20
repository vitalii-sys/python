vyruchka = int(input('Введите Вашу выручку: '))
izderzhki = int(input('Введите Ваши издержки: '))

if vyruchka > izderzhki:
    pribyl = vyruchka - izderzhki
    rentabelnost = pribyl / vyruchka
    print(f'Работаем в прибыль.\nРентабельность:{rentabelnost}')
    chislosotrudnikov = int(input('Введите численность сотрудников фирмы: '))
    pribylchel = pribyl / chislosotrudnikov
    print(f'Прибыль на одного сотрудника:{pribylchel}')
elif izderzhki > vyruchka:
    print('Работаем в убыток.')
else:
    print('Работаем на самоокупаемость.')
