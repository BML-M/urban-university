def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для результатов

    for func in functions:
        results[func.__name__] = func(int_list)  # Вызываем функцию и записываем результат в словарь

    return results  # Возвращаем словарь с результатами

# Примеры вызовов функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))