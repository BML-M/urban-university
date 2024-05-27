def calculate_structure_sum(*args):
    total_sum = 0

    # Перебираем каждый элемент входных данных
    for arg in args:
        if isinstance(arg, int):  # Если элемент является числом
            total_sum += arg
        elif isinstance(arg, str):  # Если элемент является строкой
            total_sum += len(arg)
        elif isinstance(arg, (list, tuple)):  # Если элемент является списком или кортежем
            total_sum += calculate_structure_sum(*arg)  # Рекурсивно вызываем функцию для элементов списка или кортежа
        elif isinstance(arg, dict):  # Если элемент является словарем
            total_sum += calculate_structure_sum(*arg.values())  # Рекурсивно вызываем функцию для значений словаря
        elif isinstance(arg, set):  # Если элемент является множеством
            total_sum += calculate_structure_sum(*arg)  # Рекурсивно вызываем функцию для элементов множества

    return total_sum


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]


result = calculate_structure_sum(*data_structure)
print(result)
