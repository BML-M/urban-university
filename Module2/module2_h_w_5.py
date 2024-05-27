def get_matrix(n, m, value):
    matrix = []  # Создаем пустой список matrix
    for _ in range(n):  # Внешний цикл для строк
        row = []  # Создаем пустой список для строки
        for _ in range(m):  # Внутренний цикл для столбцов
            row.append(value)  # Добавляем значение в строку
        matrix.append(row)  # Добавляем строку в матрицу
    return matrix  # Возвращаем матрицу


# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результата
print(result1)
print(result2)
print(result3)
