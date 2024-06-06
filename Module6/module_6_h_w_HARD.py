class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __is_valid_sides(self, *sides):
        return all(side > 0 for side in sides) and len(sides) == self.sides_count

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height(*sides)

    def __calculate_height(self, a, b, c):
        s = sum(sides) / 2
        return (2 / a) * (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_square(self):
        s = sum(self.__sides) / 2
        return (s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, side)
        self.__sides = [side] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3

# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.set_sides())
print(circle1.set_sides())

# Проверка периметра (круга), это и есть длина
print(len(circle1))

# Проверка объема (куба)
print(cube1.get_volume())
