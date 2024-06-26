import os
import time

directory = r'D:\urban-university\urban-university\Module7'  # Путь к каталогу с использованием сырых строк (raw string)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize_1 = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize_1} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
