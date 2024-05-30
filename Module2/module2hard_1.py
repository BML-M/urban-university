n = int(input("Введите число от 3 до 20: "))  # Запрашиваем число n

numbers = list(range(1, n))  # Создаем список чисел от 1 до n
pairs = []  # Создаем пустой список для пар чисел

for i in range(len(numbers)):  # Перебираем все числа в списке numbers
    for j in range(i + 1, len(numbers)):  # Перебираем все числа, начиная с i+1, в списке numbers
        if numbers[i] + numbers[j] == n:
            pairs.append(str(numbers[i]))  # Добавляем первое число в пары
            pairs.append(str(numbers[j]))  # Добавляем второе число в пары
            continue

        if n % (numbers[i] + numbers[j]) == 0:
            pairs.append(str(numbers[i]))  # Добавляем первое число в пары
            pairs.append(str(numbers[j]))  # Добавляем второе число в пары

result = "".join(pairs)  # Объединяем чи20сла в парах в одну строку
print(result)  # Выводим результат
