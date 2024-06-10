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
            int(input("Введите целое число: "))
            print("Данные успешно обработаны.")
            break
        except ValueError:
            print("Ошибка: Введенные данные не являются целым числом")
        except InvalidDataException as e:
            print("Ошибка: Неверные данные -", e)
        except ProcessingException as e:
            print("Ошибка при обработке данных -", e)


# Вызовем функцию для обработки данных
process_data()
