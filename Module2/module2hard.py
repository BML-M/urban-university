n = int(input("Введите число от 3 до 20: "))  # Запрашиваем число n

numbers = list(range(1, n + 1))  # Создаем список чисел от 1 до n
pairs = []  # Создаем пустой список для пар чисел

for i in range(len(numbers)):  # Перебираем все числа в списке numbers
    for j in range(i + 1, len(numbers)):  # Перебираем все числа, начиная с i+1, в списке numbers
        if numbers[i] + numbers[j] == n and numbers[
            j] not in pairs:  # Если сумма чисел равна n и второе число не в парах
            pairs.append(numbers[i])  # Добавляем первое число в пары
            pairs.append(numbers[j])  # Добавляем второе число в пары

result = "".join(str(x) for x in pairs)  # Преобразуем числа в парах в строку
print(result)  # Выводим результат
