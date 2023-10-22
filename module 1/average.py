a, b = int(input()), int(input())

count = 0
sum = 0
for i in range(a, b):
    if i % 3 == 0:
        sum += i
        count += 1

print(f'Среднее значение от {a} до {b}: {sum / count}')