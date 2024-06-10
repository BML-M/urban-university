# Задача 1: Фабрика Функций
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract

my_func_add = create_operation("add")
my_func_subtract = create_operation("subtract")
print(my_func_add(1, 2))  # Выводит 3
print(my_func_subtract(5, 3))  # Выводит 2

# Задача 2: Лямбда-Функции
square_lambda = lambda x: x ** 2
print(square_lambda(4))  # Выводит 16

def square_def(x):
    return x ** 2
print(square_def(4))  # Выводит 16

# Задача 3: Вызываемые Объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

rect = Rect(3, 4)
print(rect())  # Выводит 12