from Circle import *
from PointLine import *


class Rectangle(object):
    """four points are defined by clockwise order from upper left corner"""

    def __init__(self, p1, p2, p3, p4):
        self.p1, self.p2, self.p3, self.p4 = p1, p2, p3, p4

    def getCenter(self):

        return Point((self.p2.x + self.p4.x) / 2, (self.p2.y + self.p4.y) / 2)

    def getXline(self):

        rectangle_center = self.getCenter()
        x_center = Point((self.p2.x + self.p3.x) / 2, (self.p2.y + self.p3.y) / 2)
        return Line(x_center, rectangle_center)

    def getYline(self):

        rectangle_center = self.getCenter()
        y_center = Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)
        return Line(y_center, rectangle_center)

      
def pointInRectangle(point, rectangle):
    """determine whether a point in a rectangle"""

    x_line = rectangle.getXline()
    y_line = rectangle.getYline()
    d1 = pointToLine(point, y_line) - pointToLine(rectangle.p2, y_line)
    d2 = pointToLine(point, x_line) - pointToLine(rectangle.p2, x_line)

    return d1 < 1e-9 and d2 < 1e-9


def segmentIntersectsRectangle(s, rectangle):
    """determine whether a segment intersects a rectangle"""

    s1 = Segment(rectangle.p1, rectangle.p2)
    s2 = Segment(rectangle.p2, rectangle.p3)
    s3 = Segment(rectangle.p3, rectangle.p4)
    s4 = Segment(rectangle.p4, rectangle.p1)

    segmentsList = [s1, s2, s3, s4]

    if pointInRectangle(s.p1, rectangle) and pointInRectangle(s.p2, rectangle):
        return True

    for segment in segmentsList:
        if segmentsIntersect(segment, s):
            return True
    return False


def lineIntersectsRectangle(l, rectangle):
    """determine whether a line intersects a rectangle"""

    s1 = Segment(rectangle.p1, rectangle.p2)
    s2 = Segment(rectangle.p2, rectangle.p3)
    s3 = Segment(rectangle.p3, rectangle.p4)
    s4 = Segment(rectangle.p4, rectangle.p1)

    segmentsList = [s1, s2, s3, s4]

    for segment in segmentsList:
        if segmentIntersectsLine(segment, l):
            return True
    return False


def circleIntersectsRectangle(circle, rectangle):
    """determine whether a circle intersects a rectangle"""

    if pointInCircle(rectangle.p1, circle) or pointInCircle(rectangle.p1, circle) or\
            pointInCircle(rectangle.p1, circle) or pointInCircle(rectangle.p1, circle):
        return True

    x_line = rectangle.getXline()
    y_line = rectangle.getYline()

    dx, dy = pointToLine(circle.center, x_line), pointToLine(circle.center, y_line)
    h, w = pointDistance(rectangle.p1, rectangle.p2), pointDistance(rectangle.p2, rectangle.p3)

    if dx - h / 2 < 1e-9 and dy - (circle.radius + w / 2) < 1e-9:
        return True

    if dy - w / 2 < 1e-9 and dx - (circle.radius + h / 2) < 1e-9:
        return True

    return False
