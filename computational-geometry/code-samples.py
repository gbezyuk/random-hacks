from math import sqrt

def frange(x, y, tabulation_step):
  while x < y:
    yield x
    x += tabulation_step

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    @property
    def abs(self):
        return sqrt(self.x * self.x + self.y * self.y)

Vector = Point;

p1 = Point( 2.0,  3.0)
p2 = Point(-3.0, -2.0)


def tabulate_convex_combination (p1, p2, tabulation_step=0.1):
    for alpha in frange(0.0, 1.0, tabulation_step):
        yield alpha, 1.0 - alpha, p1.x * alpha + (1.0 - alpha) * p2.x, p1.y * alpha + (1.0 - alpha) * p2.y


def cross_product(v1, v2):
    return Vector(v1.x * v2.y, v1.y * v2.x)

v3 = cross_product(p1, p2)
print(p1, p1.abs)
print(p2, p2.abs)
print(v3, v3.abs)