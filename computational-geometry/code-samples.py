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
        return self.__str__()

    @property
    def abs(self):
        return sqrt(self.x * self.x + self.y * self.y)

Vector = Point;

p1 = Point( 2.0,  3.0)
p2 = Point(-3.0, -2.0)


class LineSegment:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return "(%s, %s), (%s, %s)" % (self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        return self.__str__()

    @property
    def vector(self):
        return Vector(self.x2 - self.x1, self.y2 - self.y1)

    @property
    def abs(self):
        return self.vector.abs


def tabulate_convex_combination (p1, p2, tabulation_step=0.1):
    for alpha in frange(0.0, 1.0, tabulation_step):
        yield alpha, 1.0 - alpha, p1.x * alpha + (1.0 - alpha) * p2.x, p1.y * alpha + (1.0 - alpha) * p2.y


def cross_product(v1, v2):
    return Vector(v1.x * v2.y, v1.y * v2.x)


def detect_intersection(ls1, ls2):
    
    def bounding_box_quick_rejection(ls1, ls2):        
        # bounding rectangle 1
        x1 = min(ls1.x1, ls1.x2)
        x2 = max(ls1.x1, ls1.x2)
        y1 = min(ls1.y1, ls1.y2)
        y2 = max(ls1.y1, ls1.y2)

        # bounding rectangle 2
        x3 = min(ls2.x1, ls2.x2)
        x4 = max(ls2.x1, ls2.x2)
        y3 = min(ls2.y1, ls2.y2)
        y4 = max(ls2.y1, ls2.y2)

        # bounding rectangle intersection condition
        return (x2 >= x3) and (x4 >= x1) and (y2 >= y3) and (y4 >= y1)

    def cross_products_differ_in_sign():
        pass 

    return bounding_box_quick_rejection(v1, v2) and
           cross_products_differ_in_sign() and
           cross_products_differ_in_sign()
