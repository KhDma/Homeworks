class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def contains(self, dot):
        return((self.x-dot.x)**2+(self.y-dot.y)**2 <= self.r**2)




from random import randint
for i in range(5):
    cir = Circle(randint(-10, 10), randint(-10, 10), randint(-10, 10))
    point = Point(randint(-10, 10), randint(-10, 10))
    print("Coordinates of Circle:", cir.x, cir.y, cir.r)
    print("Coordinates of Point:", point.x, point.y)
    print(cir.contains(point), "\n")
