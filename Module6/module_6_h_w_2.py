class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 200

class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1500000
        self.vehicle_type = "Седан"

    def horse_powers(self):
        return 250

nissan_car = Nissan()
print("\033[92mМарка машины: Nissan\033[0m")
print("Тип транспортного средства:", nissan_car.vehicle_type)
print("Цена:", nissan_car.price)
print("Количество ЛС:", nissan_car.horse_powers())