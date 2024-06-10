class InvalidDataException(Exception):
    def __init__(self, message="Invalid Data Exception"):
        self.message = message
        super().__init__(self.message)


class ProcessingException(Exception):
    def __init__(self, message="Processing Exception"):
        self.message = message
        super().__init__(self.message)



def process_data():
    while True:
        try:
            data = int(input("Введите целое число: "))
            # Здесь можно добавить код для обработки данных
            if data < 0:
                raise InvalidDataException("Число не может быть отрицательным")
            print("Данные успешно обработаны.")
            break  # Выход из цикла, если данные успешно обработаны
        except ValueError:
            print("Ошибка: Введенные данные не являются целым числом")
        except InvalidDataException as e:
            print("Ошибка: Неверные данные -", e)
            raise e  # Передаем исключение в вызывающую функцию
        except ProcessingException as e:
            print("Ошибка при обработке данных -", e)
            raise e  # Передаем исключение в вызывающую функцию

# Вызовем функцию для обработки данных
try:
    process_data()
except InvalidDataException as e:
    print("Обработанное исключение в вызывающей функции -", e)
except ProcessingException as e:
    print("Обработанное исключение в вызывающей функции -", e)