class Figure:
    sides_count = 0

    def init(self, color, *sides):
        # Проверка количества сторон и установка значений по умолчанию, если необходимо
        if len(sides) != self.sides_count:
            self.sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= val <= 255 for val in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __is_valid_sides(self, *sides):
        return all(isinstance(val, int) and val > 0 for val in sides) and len(sides) == self.sides_count

    def __len(self):
        return sum(self.sides)


class Circle(Figure):
    sides_count = 1

    def __init(self, color, radius):
        super().init(color, radius)

    def get_square(self):
        return 3.14 * (self.__sides[0] ** 2)

    def get_sides(self):
        return self.sides


class Triangle(Figure):
    sides_count = 3

    def __init(self, color, *sides):
        super().init(color, *sides)

    def get_square(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        return (p * (p - a) *p - b) * (p - c) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init(self, color, side_length):
        sides = [side_length] * self.sides_count
        super().init(color, *sides)

    def get_volume(self):
        return self._Figure__sides[0]**3

    def get_sides(self):
        return self._Figure__sides

# Создание объектов circle1 (круг) и cube1 (куб) с определенными характеристиками
