from Rectangle import *
p1 = Point(3, 2)
p2 = Point(3, 4)
p3 = Point(5, 4)
p4 = Point(5, 2)

circle = Circle(Point(1, 1), 1)
rect = Rectangle(p1, p2, p3, p4)

print(circleIntersectsRectangle(circle, rect))