import threading
import time
from colorama import init, Back, Fore, Style

init(autoreset=True)


class Knight(threading.Thread):
    def __init__(self, name, skill, color):  # Corrected the init method
        super().__init__()
        self.name = name
        self.skill = skill
        self.color = color

    def run(self):
        print(getattr(Back, self.color) + f"{self.name}, на нас напали!" + Style.RESET_ALL)
        enemies = 100
        days = 0

        while enemies > 0:
            days += 1
            enemies -= self.skill
            print(getattr(Fore, self.color
                          ) + f"{self.name}, сражается {days} день(дня)..., осталось {enemies} воинов." + Style.RESET_ALL
                  )
            time.sleep(1.5)

        print(getattr(Back, self.color) + f"{self.name} одержал победу спустя {days} дней!" + Style.RESET_ALL)


class Archer(Knight):  # Archer class inheriting from Knight class
    def __init__(self, name, skill, color):  # Archer class with init method
        super().__init__(name, skill, color)

    def run(self):
        print(getattr(Back, self.color) + f"{self.name}, на нас напали!" + Style.RESET_ALL)
        enemies = 100
        days = 0

        while enemies > 0:
            days += 1
            enemies -= self.skill
            print(getattr(Fore, self.color
                          ) + f"{self.name}, стреляет {days} день(дня)..., осталось {enemies} воинов." + Style.RESET_ALL
                  )
            time.sleep(2)

        print(getattr(Back, self.color) + f"{self.name} одержал победу спустя {days} дней!" + Style.RESET_ALL)


knight1 = Knight("Sir Lancelot", 10, "GREEN")  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20, "RED")  # Высокий уровень умения
archer1 = Archer("Robin Hood", 15, "BLUE")  # Средний уровень умения
archer2 = Archer("Legolas", 25, "MAGENTA")  # Высокий уровень умения

knight1.start()
knight2.start()
archer1.start()
archer2.start()

knight1.join()
knight2.join()
archer1.join()
archer2.join()

print("Все битвы закончились!")
