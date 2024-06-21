import threading
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Customer(threading.Thread):
    def __init__(self, number, table):
        super().__init__()
        self.number = number
        self.table = table

    def run(self):
        print(f"Посетитель номер {self.number} сел за стол {self.table.number}.")
        time.sleep(5)  # время на прием пищи
        self.table.is_busy = False
        print(f"Посетитель номер {self.number} покушал и ушёл.")

class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = [Table(number) for number in range(1, tables)]

    def customer_arrival(self):
        if not self.queue.empty():
            next_customer = self.queue.get()
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    next_customer.table = table
                    next_customer.start()
                    return
        else:
            for table in self.tables:
                if not table.is_busy:
                    customer = Customer(table.number, table)
                    table.is_busy = True
                    customer.start()
                    return
            print("Все столы заняты. Посетитель пошел в очередь.")
            self.queue.put(Customer(self.queue.qsize() + 1, None))

    def serve_customer(self, customer):
        if not self.queue.empty():
            next_customer = self.queue.get()
            next_customer.table = customer.table
            next_customer.start()

cafe = Cafe(3)
for i in range(1, 21):
    cafe.customer_arrival()
    time.sleep(2)
