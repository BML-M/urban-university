class House:
    def __init__(self, name, number_of_floors):  # Определение метода инициализации объекта
        self.name = name  # Присвоение переданного названия объекту
        self.number_of_floors = number_of_floors  # Присвоение переданного количества этажей объекту

    def go_to(self, new_floor):  # Определение метода для перемещения на нужный этаж
        if new_floor <= self.number_of_floors and new_floor >= 1:  # Проверка, что этаж существует
            for i in range(1, new_floor+1):  # Цикл от 1 до new_floor включительно
                print(i)  # Вывод текущего этажа
        else:
            print("Такого этажа не существует")  # Вывод сообщения об ошибке

# Пример использования
h1 = House('ЖК Усть-Ухта', 18)  # Создание объекта h1
h2 = House('Домик в деревне', 2)  # Создание объекта h2
print(h1.name, h1.number_of_floors)  # Печать названия и количества этажей объекта h1
print(h2.name, h2.number_of_floors)  # Печать названия и количества этажей объекта h2
h1.go_to(5)  # Вызов метода go_to для объекта h1
h2.go_to(10)  # Вызов метода go_to для объекта h2