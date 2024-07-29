def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для подходящих слов
    root_word_lower = root_word.lower()  # Приводим корневое слово к нижнему регистру для сравнения

    for word in other_words:
        word_lower = word.lower()  # Приводим каждое слово из списка к нижнему регистру
        # Проверяем, содержится ли корневое слово в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список, если условие выполняется

    return same_words  # Возвращаем список подходящих слов


# Примеры вызовов функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на экран
print(result1)
print(result2)