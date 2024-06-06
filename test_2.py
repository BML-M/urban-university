class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
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

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)

    def get_square(self):
        return 3.14 * (self.__sides[0] ** 2)

    def get_sides(self):
        return self.sides


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return (p * (p - a) *p - b) * (p - c) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        sides = [side_length] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self._Figure__sides[0] ** 3

    def get_sides(self):
        return self._Figure__sides
# class Cube(Figure):
#     sides_count = 12
#
#     def __init__(self, color, side_length):
#         sides = [side_length] * self.sides_count
#         super().__init__(color, *sides)
#
#     def get_volume(self):
#         return self.__sides[0] ** 3




circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)

print(circle1.get_color())
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)

print(cube1._Figure__sides)
print(circle1._Figure__sides)

print(len(circle1))
print(cube1.get_volume())
