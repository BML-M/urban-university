class Building:
    def __init__(self, numberOfFloors, buildingType):  # Инициализатор класса Building
        self.numberOfFloors = numberOfFloors  # Устанавливаем атрибут этажности
        self.buildingType = buildingType  # Устанавливаем атрибут типа здания

    def __eq__(self, other):  # Перегрузка оператора равенства
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType  # Сравниваем атрибуты этажности и типа здания


# Создаем два объекта Building для сравнения
building1 = Building(5, 'Residential')
building2 = Building(5, 'Appartaments')

# Проверяем равенство объектов
if building1 == building2:
    print('Оба здания имеют одинаковое количество этажей и тип')
else:
    print('Здания различаются')