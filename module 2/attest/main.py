from calc import plus, minus, divider, div, whole

print('Приветствую в калькуляторе!\n Введите 2 числа по очередности и выберите операцию:')
a = float(input('Первое число: '))
b = float(input('Второе число: '))

print('Выберите операцию:\n % - остаток от деления\n + - сложение\n - - вычитание\n // - целочисленное деление\n / - деление ')
operation = str(input())
try:
    if operation == '/':
        print(divider(a, b))
    if operation == '%':
        print(div(a, b))
    if operation == '+':
        print(plus(a, b))
    if operation == '-':
        print(minus(a, b))
    if operation == '//':
        print(whole(a, b))
except:
    raise KeyboardInterrupt(f'Ваша операция {operation} не поддерживается в данном калькуляторе')