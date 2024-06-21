import threading


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity

    def run(self, requests):
        threads = []
        for request in requests:
            thread = threading.Thread(target=self.process_request, args=(request,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("Пряники", "receipt", 100),
    ("Морковки", "receipt", 150),
    ("Пряники", "shipment", 30),
    ("Картохи", "receipt", 200),
    ("Морковки", "shipment", 50)
    ]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)
