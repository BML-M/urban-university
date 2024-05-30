n = int(input("Введите число от 3 до 20: "))  # Запрашиваем число n

numbers = list(range(1, n))  # Создаем список чисел от 1 до n
pairs = []  # Создаем пустой список для пар чисел

i = 0
while i < len(numbers):  # Пока не перебраны все числа в списке numbers
    j = i + 1
    while j < len(numbers):  # Пока не перебраны все числа, начиная с i+1, в списке numbers
        if numbers[i] + numbers[j] == n:
            pairs.append(str(numbers[i]))  # Добавляем первое число в пары
            pairs.append(str(numbers[j]))  # Добавляем второе число в пары
            j += 1
            continue

        if n % (numbers[i] + numbers[j]) == 0:  # Проверяем условие: если n делится на сумму numbers[i] и numbers[j] без остатка
            pairs.append(str(numbers[i]))  # Добавляем первое число в пары
            pairs.append(str(numbers[j]))  # Добавляем второе число в пары
        j += 1
    i += 1

result = "".join(pairs)  # Объединяем числа в парах в одну строку
print(result)  # Выводим результат
