import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def __contains__(self, point):
        distance = math.sqrt((self.center.x - point.x)**2 + (self.center.y - point.y)**2)
        return distance <= self.radius


circle = Circle(1, 2, 10)
point = Point(1, 2)

print(point in circle)