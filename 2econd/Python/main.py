from math import pi


class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, ax, ay, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = ax
        self.by = cy
        self.cx = cx
        self.cy = cy
        self.dx = cx
        self.dy = ay
        self.horizontal = cx - ax
        self.vertical = cy - ay

    def area(self):
        return self.horizontal * self.vertical

    def perimeter(self):
        return 2*(self.horizontal+self.vertical)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    print("""Так розташовані вугли прямокутника
    B--------C
    |        |
    |        |
    A--------D""")

    ax = 0.0
    ay = 0.0
    cx = 40.0
    cy = 15.0
    rectangle = Rectangle(ax, ay, cx, cy)
    print(f"A(x) = {ax}\n"
          f"A(y) = {ay}\n"
          f"C(x) = {cx}\n"
          f"C(y) = {cy}")
    print(f"Площа прямокутника = {round(rectangle.area(), 4)}")
    print(f"Периметр прямокутника = {round(rectangle.perimeter(), 4)}\n")

    radius = 18.00
    circle = Circle(radius)
    print(f"Площа кругу = {round(circle.area(), 4)}")
    print(f"Периметр кругу = {round(circle.perimeter(), 4)}")