class House:
    def __init__(self):  # Инициализатор класса House
        self.numberOfFloors = 0  # Устанавливаем атрибут этажности по умолчанию равным 0

    def setNewNumberOfFloors(self, floors):  # Метод для изменения числа этажей
        self.numberOfFloors = floors  # Устанавливаем новое значение для числа этажей
        print("Number of floors has been updated to", self.numberOfFloors
              )  # Выводим сообщение о обновлении числа этажей


# Создаем экземпляр класса House
my_house = House()
# Вызываем метод setNewNumberOfFloors для обновления числа этажей до 5
my_house.setNewNumberOfFloors(5)