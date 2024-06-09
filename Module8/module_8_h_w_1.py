def add_everything_up(a, b):
    try:
        # Проверяем, что типы данных a и b не равны
        if type(a) != type(b):
            return str(a) + str(b)  # Возвращаем строковое представление a и b
        else:
            return a + b  # Складываем a и b
    except TypeError:
        return str(a) + str(b)  # В случае ошибки возвращаем строковое представление a и b


# Примеры использования функции
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
