import sys

def circular_array_path(n, m):
    path = [1]  # начинаем с первого элемента
    pos = 1  # текущая позиция
    while True:
        pos = (pos + m - 1) % n  # вычисляем новую позицию
        if pos == 0:  # если новая позиция в начале массива
            pos = n  # заменяем 0 на n
        if pos == 1:  # если достигли начала массива
            break  # прекращаем цикл
        path.append(pos)  # добавляем текущую позицию в путь
    return path

n = int(sys.argv[1])
m = int(sys.argv[2])

print(''.join(map(str, circular_array_path(n, m))))