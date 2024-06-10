def all_variants(s):
    n = len(s)  # Определяем длину строки s
    for i_main in range(1, 2 ** n):  # Проходим по всем возможным подмножествам строки s
        subset = ''  # Создаем пустую строку subset для хранения подпоследовательности
        for j in range(n):  # Проходим по каждому символу в строке s
            if (i_main >> j) % 2:  # Проверяем, присутствует ли символ в подмножестве
                subset += s[j]  # Добавляем символ к подпоследовательности
        yield subset  # Возвращаем подпоследовательность через оператор yield


a = all_variants("abc")  # Создаем объект-генератор, передавая строку "abc"
for i in a:  # Проходим по всем элементам, возвращаемым генератором a
    print(i)  # Выводим текущую подпоследовательность на экран



'''
1. Функция `all_variants` принимает строку `s` и генерирует все возможные подпоследовательности этой строки.
2. Переменная `n` содержит длину строки `s`.
3. Цикл `for i_main in range(1, 2 ** n):` проходит по всем возможным подмножествам строки `s`.
4. Внутренний цикл `for j in range(n):` проходит по каждому символу в строке `s`.
5. Условие `(i_main >> j) % 2` проверяет, присутствует ли символ с индексом `j` в подмножестве с номером `i`.
6. Если символ присутствует в подмножестве, он добавляется к подпоследовательности `subset`.
7. Оператор `yield subset` возвращает текущую подпоследовательность.
8. Создается объект-генератор `a`, передавая ему строку "abc".
9. Цикл `for i in a:` проходит по всем подпоследовательностям, возвращаемым генератором `a`.
10. Каждая подпоследовательность выводится на экран с помощью `print(i)`.
Этот код позволяет получить и вывести все возможные подпоследовательности строки "abc".'''