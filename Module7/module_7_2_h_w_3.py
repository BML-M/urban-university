def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(index, position)] = string

    return strings_positions


# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Вызов функции с указанием имени файла
result = custom_write('test.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)