class Car:
    def __init__(self, brand):
        self.brand = brand
        self.price = 1000000  # Устанавливаем базовую цену для всех автомобилей

    def horse_powers(self):
        return 200  # Возвращаем количество лошадиных сил для всех автомобилей


class Nissan(Car):
    def __init__(self):
        super().__init__('Nissan')
        self.price = 1500000  # Устанавливаем новую цену для автомобилей Nissan

    def horse_powers(self):
        return 250  # Переопределяем количество лошадиных сил для автомобилей Nissan


class Kia(Car):
    def __init__(self):
        super().__init__('Kia')
        self.price = 1200000  # Устанавливаем новую цену для автомобилей Kia

    def horse_powers(self):
        return 180  # Переопределяем количество лошадиных сил для автомобилей Kia


# Пример использования:
car = Car('Generic Car')
print(f"{car.brand}, Цена по прайсу: {car.price}$, Количество лошадиных сил: {car.horse_powers()}"
      )  # Generic Car, Цена по прайсу: 1000000$, Количество лошадиных сил: 200

nissan = Nissan()
print(
    f"\033[92m{nissan.brand}\033[0m, Цена по прайсу: {nissan.price}$, Количество лошадиных сил: {nissan.horse_powers()}"
    )  # Nissan, Цена по прайсу: 1500000$, Количество лошадиных сил: 250

kia = Kia()
print(f"\033[91m{kia.brand}\033[0m, Цена по прайсу: {kia.price}$, Количество лошадиных сил: {kia.horse_powers()}"
      )  # Kia, Цена по прайсу: 1200000$, Количество лошадиных сил: 180
