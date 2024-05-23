# Запрашиваем у пользователя ввести текст и присваиваем его переменной my_string
my_string = input("Введите текст: ")

# Вывести длину символов введённого текста:
print("Длина текста:", len(my_string))

# Работа с методами строк:
# Вывести строку my_string в верхнем регистре:
print("Текст в верхнем регистре:", my_string.upper())

# Вывести строку my_string в нижнем регистре:
print("Текст в нижнем регистре:", my_string.lower())

# Изменяем строку my_string, удалив все пробелы:
my_string_without_spaces = my_string.replace(" ", "")
print("Текст без пробелов:", my_string_without_spaces)

# Вывести первый символ строки my_string:
print("Первый символ:", my_string[0])

# Вывести последний символ строки my_string:
print("Последний символ:", my_string[-1])