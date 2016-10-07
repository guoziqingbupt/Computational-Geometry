from PointLine import *


class Circle(object):
    """Circle has 2 attributes: center and radius"""

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def pointInCircle(point, circle):
    """determine whether a point in a circle"""

    return (pointDistance(point, circle.center) - circle.radius) < 1e-9


def lineIntersectsCircle(line, circle):
    """determine whether a line intersects a circle"""

    dis = pointToLine(circle.center, line)
    return dis - circle.radius < 1e-9


def segmentIntersectsCircle(AB, circle):
    """determine whether a segment intersects a circle"""

    if not lineIntersectsCircle(Line(AB.p1, AB.p2), circle):
        return False

    if pointInCircle(AB.p1, circle) or pointInCircle(AB.p2, circle):
        return True
    
    vector_AB = Vector(AB.p1, AB.p2)
    vector_AO = Vector(AB.p1, circle.center)

    # two ndarray object
    tAB = np.array([vector_AB.x, vector_AB.y])
    tAO = np.array([vector_AO.x, vector_AO.y])

    # vector AD, type: ndarray
    tAD = ((tAB @ tAO) / (tAB @ tAB)) * tAB

    # get point D
    Dx, Dy = tAD[0] + AB.p1.x, tAD[1] + AB.p1.y
    D = Point(Dx, Dy)

    return pointInCircle(D, circle) and pointInSegment(D, AB)


