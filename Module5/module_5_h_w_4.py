class Building:
    total = 0  # Атрибут для хранения общего количества созданных объектов класса Building

    def __init__(self, name):
        self.name = name  # Атрибут для хранения имени объекта Building
        Building.total += 1  # Увеличиваем атрибут total при создании нового объекта Building


# Цикл для создания 40 объектов класса Building с различными именами и выводом на экран
for i in range(40):
    building_name = f"Building_{i + 1}"  # Генерируем имя объекта Building
    building = Building(building_name)
    print(building.name)

print("Общее количество объектов Building:", Building.total)