def IsPrime(n) -> str:
    count = 0
    for divider in range(1, n):
        if n % divider == 0:
            print(f'Делитель {n}: {divider}')
            count += 1
    
    if count <= 2:
        return 'Простое'
    else:
        return 'Обычное'