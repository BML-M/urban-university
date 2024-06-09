numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Используем map для возведения чисел в квадрат
squared_numbers = map(lambda x: x ** 2, numbers)

# Используем filter для отбора нечетных чисел
odd_squared_numbers = filter(lambda x: x % 2 != 0, squared_numbers)

# Преобразуем генератор в список для вывода результата
result = list(odd_squared_numbers)

print(result)