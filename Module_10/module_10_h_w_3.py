import threading
from threading import Lock


class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = Lock()  # Создаем объект блокировки

    def deposit(self, amount):
        with self.lock:  # Устанавливаем блокировку
            self.balance += amount
            print(f"Пополнено на {amount}, новый баланс: {self.balance}")

    def withdraw(self, amount):
        with self.lock:  # Устанавливаем блокировку
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снято {amount}, новый баланс: {self.balance}")
            else:
                print("Недостаточно средств для снятия")


def deposit_task(account_x, amount):
    for _ in range(5):
        account_x.deposit(amount)


def withdraw_task(account_x, amount):
    for _ in range(5):
        account_x.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
