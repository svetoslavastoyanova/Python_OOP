import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        distance_x = self.x - x
        distance_y = self.y - y
        c = math.sqrt(distance_y**2 + distance_x**2)
        return c


p = Point(2, 4)
print(p.set_x(3))
print(p.set_y(5))
print(p.distance(10, 2))
