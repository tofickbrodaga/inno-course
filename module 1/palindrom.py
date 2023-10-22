digit = int(input('Введите число:'))
temp = digit
reverse = 0

while(digit > 0):
    n = digit % 10
    reverse = reverse * 10 + n
    digit = digit // 10
if(temp == reverse):
    print('Это палиндром')
else:
    print('Это не палиндром')