class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self._file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self._file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()  # Возвращаем строку с продуктами
        except FileNotFoundError:
            return ""  # Если файл не найден, возвращаем пустую строку

    def add(self, *products):
        existing_products = self.get_products().splitlines() if self.get_products() else []

        for product in products:
            product_str = str(product)
            product_name = product.name

            # Проверяем, существует ли продукт в магазине
            if any(product_name in existing for existing in existing_products):
                print(f"Продукт {product_name} уже есть в магазине")
            else:
                with open(self._file_name, 'a', encoding='utf-8') as file:
                    file.write(product_str + '\n')  # Записываем новый продукт в файл
                existing_products.append(product_str)  # Добавляем в список существующих продуктов


# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Картошка', 50.5, 'Овощ')
    p2 = Product('Спагетти', 3.4, 'Макаронные изделия')
    p3 = Product('мелкая Картошка', 5.5, 'Овощ')

    print(p2)  # Вывод: Spaghetti, 3.4, Groceries

    s1.add(p1, p2, p3)
    print(s1.get_products())  # Вывод всех продуктов

    # Второй запуск для проверки существующих продуктов
    s1.add(p1, p2, p3)
    print(s1.get_products())  # Вывод всех продуктов снова