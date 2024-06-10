import threading
import time


# Функция print_numbers выводит числа от 1 до 27 с интервалом в 1.01 секунду
def print_numbers():
    for i in range(1, 27):
        print(i)
        time.sleep(1.015)


# Функция print_letters выводит буквы от 'a' до 'z' с интервалом в 1 секунду
def print_letters():
    for letter in range(ord('a'), ord('z') + 1):
        print(chr(letter))
        time.sleep(1.018)


# Создание двух потоков, каждый со своей функцией-целью
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Запуск потоков
thread1.start()
thread2.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()
