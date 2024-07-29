def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл в режиме записи с указанием кодировки utf-8
    file = open(file_name, 'w', encoding='utf-8')  # Открываем файл

    for index, string in enumerate(strings, start=1):
        position = file.tell()  # Получаем текущую позицию в файле
        file.write(string + '\n')  # Записываем строку в файл
        strings_positions[(index, position)] = string  # Сохраняем информацию о строке

    file.close()  # Закрываем файл

    return strings_positions  # Возвращаем словарь с позициями строк


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