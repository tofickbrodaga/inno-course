digit = int(input())

factorial = 1
while digit > 0:
    factorial *= digit
    digit -= 1

print(factorial)