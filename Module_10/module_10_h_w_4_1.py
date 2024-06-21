import threading
import time
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.visitors_count = 0
        self.queue_count = 0

    def customer_arrival(self):
        customer_count = 1
        while self.visitors_count <= 10:
            time.sleep(1)
            print(f"\033[94mПосетитель номер {customer_count} прибыл.\033[0m")  # Цвет для прибывшего посетителя
            if self.visitors_count < len(self.tables):
                customer = threading.Thread(target=self.serve_customer, args=(customer_count,))
                customer.start()
            else:
                self.queue.put(customer_count)
                self.queue_count += 1
                print(f"\033[93mПосетитель номер {customer_count} ожидает свободный стол. Людей в очереди: {self.queue_count}\033[0m")  # Цвет для посетителя в очереди
            customer_count += 1
            self.visitors_count += 1

        print("\033[91mДостигнуто максимальное количество посетителей. Прием новых посетителей завершен.\033[0m")  # Цвет для окончания приема посетителей

    def serve_customer(self, customer_number):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"\033[92mПосетитель номер {customer_number} сел за стол {table.number}.\033[0m")  # Цвет для посетителя за столом
                time.sleep(5)
                print(f"\033[92mПосетитель номер {customer_number} покушал и ушел.\033[0m")  # Цвет для посетителя после еды
                table.is_busy = False
                self.visitors_count -= 1
                if self.queue_count > 0:
                    next_customer = self.queue.get()
                    self.queue_count -= 1
                    customer = threading.Thread(target=self.serve_customer, args=(next_customer,))
                    customer.start()
                break
        else:
            self.queue.put(customer_number)
            self.queue_count += 1
            print(f"\033[93mПосетитель номер {customer_number} ожидает свободный стол. Людей в очереди: {self.queue_count}\033[0m")  # Цвет для посетителя в очереди

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()