a = [1, 2, 3, 4, 5, 6]

for i in range(len(a)):
     x = a.pop(0)
     if not x % 2:
         a.append(x // 2)
print(a)