def task(n):
    tasks = []
    for i in range(n):
        task = input(f'Введите задачу {i+1}: ')
        tasks.append(task)

    with open('tasks.txt', 'w') as file:
        for i in range(0, len(tasks), 2):
            file.write(tasks[i])
            if i+1 < len(tasks):
                file.write(', ' + tasks[i+1])
    file.close()
