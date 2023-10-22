month = int(input('Введите месяц с 1 по 12: '))

if month == 1 or month == 2 or month == 12:
    print('Зима')
elif month == 3 or month == 4 or month == 5:
    print('Весна')
elif month == 6 or month == 7 or month == 8:
    print('Лето')
elif month > 12:
    print('В году 12 месяцев')
else:
    print('Оcень')