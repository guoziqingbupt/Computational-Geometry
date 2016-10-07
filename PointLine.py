import numpy as np
# numpy help us do some vector calculation


class Point(object):
    """Point are two-dimension"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment(object):
    """the 2 points p1 and p2 are unordered"""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Line(object):
    """p1 and p2 are 2 points in straight line"""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Vector(object):
    """start and end are two points"""

    def __init__(self, start, end):
        self.x = end.x - start.x
        self.y = end.y - start.y


def pointDistance(p1, p2):
    """calculate the distance between point p1 and p2"""

    # v: a Vector object
    v = Vector(p1, p2)

    # translate v to a ndarray object
    t = np.array([v.x, v.y])

    # calculate the inner product of ndarray t
    return float(np.sqrt(t @ t))


def pointToLine(C, AB):
    """calculate the shortest distance between point C and straight line AB, return: a float value"""

    # two Vector object
    vector_AB = Vector(AB.p1, AB.p2)
    vector_AC = Vector(AB.p1, C)

    # two ndarray object
    tAB = np.array([vector_AB.x, vector_AB.y])
    tAC = np.array([vector_AC.x, vector_AC.y])

    # vector AD, type: ndarray
    tAD = ((tAB @ tAC) / (tAB @ tAB)) * tAB

    # get point D
    Dx, Dy = tAD[0] + AB.p1.x, tAD[1] + AB.p1.y
    D = Point(Dx, Dy)

    return pointDistance(D, C)


def pointInLine(C, AB):
    """determine whether a point is in a straight line"""

    return abs(crossProduct(Vector(AB.p1, C), Vector(AB.p1, AB.p2))) < 1e-9


def pointInSegment(C, AB):
    """determine whether a point is in a segment"""

    # if C in segment AB, it first in straight line AB
    if pointInLine(C, Line(AB.p1, AB.p2)):
        return min(AB.p1.x, AB.p2.x) <= C.x <= max(AB.p1.x, AB.p2.x) \
               and min(AB.p1.y, AB.p2.y) <= C.y <= max(AB.p1.y, AB.p2.y)
    return False


def linesAreParallel(l1, l2):
    """determine whether 2 straight lines l1, l2 are parallel"""

    v1 = Vector(l1.p1, l1.p2)
    v2 = Vector(l2.p1, l2.p2)

    return abs((v1.y / v1.x) - (v2.y / v2.x)) < 1e-9


def crossProduct(v1, v2):
    """calculate the cross product of 2 vectors"""

    # v1, v2 are two Vector object
    return v1.x * v2.y - v1.y * v2.x


def segmentsIntersect(s1, s2):
    """determine whether 2 segments s1, s2 intersect with each other"""

    v1 = Vector(s1.p1, s1.p2)
    v2 = Vector(s2.p1, s2.p2)

    t1 = Vector(s1.p1, s2.p1)
    t2 = Vector(s1.p1, s2.p2)

    d1 = crossProduct(t1, v1)
    d2 = crossProduct(t2, v1)

    t3 = Vector(s2.p1, s1.p1)
    t4 = Vector(s2.p1, s1.p2)

    d3 = crossProduct(t3, v2)
    d4 = crossProduct(t4, v2)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True

    if d1 == 0:
        return pointInSegment(s2.p1, s1)
    elif d2 == 0:
        return pointInSegment(s2.p2, s1)
    elif d3 == 0:
        return pointInSegment(s1.p1, s2)
    elif d4 == 0:
        return pointInSegment(s1.p2, s2)

    return False


def segmentIntersectsLine(segment, line):

    v1 = Vector(line.p1, segment.p1)
    v2 = Vector(line.p1, line.p2)
    v3 = Vector(line.p1, segment.p2)

    d1 = crossProduct(v1, v2)
    d2 = crossProduct(v3, v2)

    return d1 * d2 <= 0
