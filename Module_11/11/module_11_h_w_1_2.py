# 2. **Анализ данных с помощью pandas:**
#    - Загрузим данные из CSV файла с помощью pandas.
#    - Выполним простой анализ данных, например, посчитаем среднее значение столбца.
#    - Выведем результат анализа.



import pandas as pd
import os

# Получаем текущий путь к файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data.csv')

# Чтение файла и создание DataFrame
data = pd.read_csv(file_path)

# Выполним простой анализ данных
# посчитаем среднее значение столбца
mean_value = data['А1'].mean()
print('Среднее значение столбца:', mean_value)
# Подсчет суммы значений в столбце
sum_value = data['А1'].sum()
print('Сумма значений в столбце:', sum_value)
# Перемножение всех значений в столбце А1
product_all = data['А1'].prod()
print('Произведение всех значений в столбце:', product_all)
