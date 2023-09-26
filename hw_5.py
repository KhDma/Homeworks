class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x0, y0, radius):
        self.x0 = x0
        self.y0 = y0
        self.radius = radius

    def contains(self, x, y):
        super().__init__(x, y)
        return((x0-x)**2+(y0-y)**2 <= self.radius**2)







x0, y0, r = map(int, input().split())
x,y = map(int, input().split())
krug = Circle(x0, y0, r)
print(krug.contains(x, y))
#krug = Circle(0, 0, 5)
#print(krug.contains(1, 1))

