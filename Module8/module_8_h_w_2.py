class CustomException1(Exception):  # Создаем собственное исключение CustomException1
    pass

class CustomException2(Exception):  # Создаем собственное исключение CustomException2
    pass

def generate_exception(argument):  # Функция, генерирующая различные исключения
    if argument == 1:
        raise CustomException1("Custom Exception 1 was raised")  # Генерируем исключение CustomException1
    elif argument == 2:
        raise CustomException2("Custom Exception 2 was raised")  # Генерируем исключение CustomException2
    else:
        raise ValueError("Invalid argument")  # Генерируем обычное исключение ValueError

def main_function(argument):  # Основная функция
    try:
        generate_exception(argument)  # Вызываем функцию generate_exception
    except CustomException1 as e:  # Обрабатываем исключение CustomException1
        print("Обработка собственного исключения 1:", e)
        raise  # Передаем исключение дальше
    except CustomException2 as e:  # Обрабатываем исключение CustomException2
        print("Обработка собственного исключения 2:", e)
        raise  # Передаем исключение дальше
    except Exception as e:  # Обрабатываем остальные исключения
        print("Обработка других исключений:", e)

try:
    main_function(1)  # Вызываем основную функцию с аргументом 1
except CustomException1 as e:  # Обрабатываем исключение CustomException1 в основной функции
    print("Обработка собственного исключения 1 в основной функции:", e)
except CustomException2 as e:  # Обрабатываем исключение CustomException2 в основной функции
    print("Обработка собственного исключения 2 в основной функции:", e)
except Exception as e:  # Обрабатываем остальные исключения в основной функции
    print("Обработка других исключений в основной функции:", e)