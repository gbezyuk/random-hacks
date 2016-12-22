def frange(x, y, tabulation_step):
  while x < y:
    yield x
    x += tabulation_step

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point( 2.0,  3.0)
p2 = Point(-3.0, -2.0)

def tabulate_convex_combination (p1, p2, tabulation_step=0.1):
    for alpha in frange(0.0, 1.0, tabulation_step):
        print alpha, 1.0 - alpha, p1.x * alpha + (1.0 - alpha) * p2.x, p1.y * alpha + (1.0 - alpha) * p2.y

tabulate_convex_combination(p1, p2)