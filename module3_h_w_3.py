def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    if len(str_number) > 1:  # Проверяем длину строки
        first = int(str_number[0])  # Получаем первую цифру числа
        return first * get_multiplied_digits(int(str_number[1:])
                                             )  # Рекурсивно умножаем первую цифру на результат для остальной части числа
    else:
        return int(str_number)  # Возвращаем оставшуюся цифру, если длина строки не больше 1


# Пример использования
result = get_multiplied_digits(485503)
print(result)
