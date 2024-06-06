class Figure:
    sides_count = 3

    def __init__(self, color, *sides):
        self.color = color
        if len(sides) != self.sides_count:
            self.sides = [1] * self.sides_count
        else:
            self.sides = list(sides)

    def get_color(self):
        return self.color

    def is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.color = (r, g, b)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides = list(new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides = list(new_sides)

    def __is_valid_sides(self, *sides):
        return all(isinstance(x, int) and x > 0 for x in sides) and len(sides) == self.sides_count

    def __is_valid_sides(self, *sides):
        return all(isinstance(x, int) and x > 0 for x in sides) and len(sides) == self.sides_count

    def __len__(self):
        return sum(self.sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)

    def get_square(self):
        return 3.14159 * self.sides[0] ** 2

    def get_sides(self):
        return self.sides


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.height = 0

    def get_square(self):
        a, b, c = self.sides
        p = sum(self.sides) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) != self.sides_count:
            self.sides = [1] * self.sides_count

    def get_volume(self):
        return self.sides[0] ** 3

    def get_sides(self):
        return self.sides

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())