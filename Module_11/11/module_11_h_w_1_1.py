# 1. **Запрос данных из API с помощью requests:**
#    - Используем библиотеку requests для получения данных о текущей погоде с открытого API.
#    - Выведем полученные данные в консоль.
# 2. **Анализ данных с помощью pandas:**
#    - Загрузим данные из CSV файла с помощью pandas.
#    - Выполним простой анализ данных, например, посчитаем среднее значение столбца.
#    - Выведем результат анализа.
#
# 3. **Математические операции с помощью numpy:**
#    - Создадим массив чисел с помощью numpy.
#    - Выполним математические операции над массивом, например, найдем сумму всех элементов массива.
#    - Выведем результат операций.
#
# 4. **Визуализация данных с помощью matplotlib:**
#    - Создадим простой график с использованием matplotlib, например, график функции.
#    - Оформим график с заголовком, подписями осей и легендой.
#
# 5. **Обработка изображений с помощью pillow:**
#    - Загрузим изображение с помощью pillow.
#    - Изменим размер изображения, применим эффекты (например, черно-белый фильтр).
#    - Сохраним измененное изображение в другом формате.

import requests


# Кельвина в Цельсия
def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15


# Преобразуем направление ветра
def convert_wind_direction(degrees):
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    index = round(degrees / 45) % 8
    return directions[index]


# Запрос данных из API с помощью requests для Москвы
response_moscow = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=fb83669082c5ff785b015bba36ef098d&lang=ru'
    )
weather_data_moscow = response_moscow.json()
# Извлечение данных о количестве осадков
if 'rain' in weather_data_moscow:
    precipitation = weather_data_moscow['rain']
elif 'snow' in weather_data_moscow:
    precipitation = weather_data_moscow['snow']
else:
    precipitation = {}

# Извлечение данных о направлении ветра, скорости ветра и облачности
wind_direction = weather_data_moscow['wind']['deg']
wind_speed = weather_data_moscow['wind']['speed']
cloudiness = weather_data_moscow['clouds']['all']

# Извлекаем температуру в Кельвинах из JSON-ответа
temp_kelvin = weather_data_moscow['main']['temp']

# Конвертируем температуру в градусы Цельсия
temp_celsius = kelvin_to_celsius(temp_kelvin)

# Определение типа облачности
if cloudiness == 0:
    cloud_type = "Ясное небо"
elif 1 <= cloudiness <= 25:
    cloud_type = "Низкая облачность"
elif 26 <= cloudiness <= 50:
    cloud_type = "Умеренная облачность"
elif 51 <= cloudiness <= 100:
    cloud_type = "Высокая облачность"

# Преобразование направления ветра
wind_direction_text = convert_wind_direction(wind_direction)

# Извлечение описания облачности
cloud_description = weather_data_moscow['weather'][0]['description']

print("Погода в Москве:")
print("Температура в Москве (в градусах Цельсия):", temp_celsius)
print("Направление ветра:", wind_direction_text)
print("Скорость ветра:", wind_speed)
print("Облачность:", cloudiness)
print("Тип облачности:", cloud_type)
print("Описание облачности:", cloud_description)

print(weather_data_moscow)
# Запрос данных из API с помощью requests для Сосногорска
response_sosnogorsk = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q=Sosnogorsk&appid=fb83669082c5ff785b015bba36ef098d&lang=ru'
    )
weather_data_sosnogorsk = response_sosnogorsk.json()

# Извлечение данных о количестве осадков
if 'rain' in weather_data_sosnogorsk:
    precipitation = weather_data_sosnogorsk['rain']
elif 'snow' in weather_data_sosnogorsk:
    precipitation = weather_data_sosnogorsk['snow']
else:
    precipitation = {}

# Извлечение данных о направлении ветра, скорости ветра и облачности
wind_direction = weather_data_sosnogorsk['wind']['deg']
wind_speed = weather_data_sosnogorsk['wind']['speed']
cloudiness = weather_data_sosnogorsk['clouds']['all']

# Извлечение температуры в Кельвинах из JSON-ответа
temp_kelvin = weather_data_sosnogorsk['main']['temp']

# Конвертируем температуру в градусы Цельсия
temp_celsius = kelvin_to_celsius(temp_kelvin)

# Определение типа облачности
if cloudiness == 0:
    cloud_type = "Ясное небо"
elif 1 <= cloudiness <= 25:
    cloud_type = "Низкая облачность"
elif 26 <= cloudiness <= 50:
    cloud_type = "Умеренная облачность"
elif 51 <= cloudiness <= 100:
    cloud_type = "Высокая облачность"

# Преобразование направления ветра
wind_direction_text = convert_wind_direction(wind_direction)

# Извлечение описания облачности
cloud_description = weather_data_sosnogorsk['weather'][0]['description']

print("Погода в Сосногорске:")
print("Температура в Сосногорске (в градусах Цельсия):", temp_celsius)
print("Направление ветра:", wind_direction_text)
print("Скорость ветра:", wind_speed)
print("Облачность:", cloudiness)
print("Тип облачности:", cloud_type)
print("Описание облачности:", cloud_description)

print(weather_data_sosnogorsk)

# Запрос данных из API с помощью requests для Лондона
response_london = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q=London&appid=fb83669082c5ff785b015bba36ef098d&lang=ru'
    )
weather_data_london = response_london.json()

# Извлечение данных о количестве осадков
if 'rain' in weather_data_london:
    precipitation = weather_data_london['rain']
elif 'snow' in weather_data_london:
    precipitation = weather_data_london['snow']
else:
    precipitation = {}

# Извлечение данных о направлении ветра, скорости ветра и облачности
wind_direction = weather_data_london['wind']['deg']
wind_speed = weather_data_london['wind']['speed']
cloudiness = weather_data_london['clouds']['all']

# Извлечение температуры в Кельвинах из JSON-ответа
temp_kelvin = weather_data_london['main']['temp']

# Конвертируем температуру в градусы Цельсия
temp_celsius = kelvin_to_celsius(temp_kelvin)
# Извлечение описания облачности
cloud_description = weather_data_london['weather'][0]['description']

# Преобразование направления ветра
wind_direction_text = convert_wind_direction(wind_direction)

# Определение типа облачности
if cloudiness == 0:
    cloud_type = "Ясное небо"
elif 1 <= cloudiness <= 25:
    cloud_type = "Низкая облачность"
elif 26 <= cloudiness <= 50:
    cloud_type = "Умеренная облачность"
elif 51 <= cloudiness <= 100:
    cloud_type = "Высокая облачность"

# Преобразование направления ветра
wind_direction_text = convert_wind_direction(wind_direction)

print("Погода в Лондоне:")
print("Температура в Лондоне (в градусах Цельсия):", temp_celsius)
print("Направление ветра:", wind_direction_text)
print("Скорость ветра:", wind_speed)
print("Облачность:", cloudiness)
print("Тип облачности:", cloud_type)
print("Описание облачности:", cloud_description)

# Вывод информации о количестве осадков
if '1h' in precipitation:
    print("Количество осадков за последний час:", precipitation['1h'])
elif '3h' in precipitation:
    print("Количество осадков за последние 3 часа:", precipitation['3h'])
else:
    print("Количество осадков не указано")
print(weather_data_london)
