def calculate_structure_sum(*args):
    # Функция для вычисления суммы значений в структуре данных с произвольным уровнем вложенности

    total_sum = 0  # Инициализация переменной для хранения общей суммы

    # Перебор аргументов функции
    for arg in args:
        if isinstance(arg, int):
            total_sum += arg  # Если значение является целым числом, добавляем его к общей сумме
        elif isinstance(arg, (list, tuple, set)):
            sub_structure_sum = calculate_structure_sum(*arg
                                                        )  # Рекурсивный вызов функции для вложенной структуры данных
            total_sum += sub_structure_sum  # Добавляем сумму вложенной структуры к общей сумме
        elif isinstance(arg, dict):
            for key, value in arg.items():
                total_sum += calculate_structure_sum(key, value)  # Вызываем функцию для ключа и значения в словаре
        elif isinstance(arg, str):
            total_sum += len(arg)  # Добавляем длину строки к общей сумме
        elif isinstance(arg, tuple):
            sub_structure_sum = calculate_structure_sum(*arg)  # Рекурсивный вызов функции для вложенной кортежа
            total_sum += sub_structure_sum  # Добавляем сумму вложенной кортежа к общей сумме

    return total_sum  # Возвращаем общую сумму


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

result = calculate_structure_sum(*data_structure)
print(result)
