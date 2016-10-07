from Circle import *
import csv


print("circle test begin...\n")
csvFile = open("GeoData_circle.csv", "r")
dict_reader = csv.DictReader(csvFile)

for dataRecord in dict_reader:

    # variable assignment
    cx = float(dataRecord["cx"])
    cy = float(dataRecord["cy"])
    radius = float(dataRecord["radius"])

    str_p1 = dataRecord["p1"]
    str_p1_list = str_p1.split(",")
    str_p2 = dataRecord["p2"]
    str_p2_list = str_p2.split(",")

    p1 = Point(float(str_p1_list[0][1:]), float(str_p1_list[1][:-1]))
    p2 = Point(float(str_p2_list[0][1:]), float(str_p2_list[1][:-1]))

    circle = Circle(Point(cx, cy), radius)

    if pointInCircle(p1, circle) != int(dataRecord["p1 in circle"]):
        print("\nin %d record, the relationship between p1 and circle is wrong!" % (dict_reader.line_num - 1))
        continue

    if pointInCircle(p2, circle) != int(dataRecord["p2 in circle"]):
        print("\nin %d record, the relationship between p2 and circle is wrong!" % (dict_reader.line_num - 1))
        continue

    if segmentIntersectsCircle(Segment(p1, p2), circle) != int(dataRecord["segment intersects circle"]):
        print("\nin %d record, the relationship between p1p2(s) and circle is wrong!" % (dict_reader.line_num - 1))
        continue

    if lineIntersectsCircle(Line(p1, p2), circle) != int(dataRecord["line intersects circle"]):
        print("\nin %d record, the relationship between p1p2(l) and circle is wrong!" % (dict_reader.line_num - 1))
        continue

    print("\nthe %d record passes the test\n" % (dict_reader.line_num - 1))

csvFile.close()

print("circle test end, point line test begin...\n")

csvFile = open("GeoData_pointline.csv", "r")
dict_reader = csv.DictReader(csvFile)

for dataRecord in dict_reader:

    # variable assignment

    str_p0 = dataRecord["p0"]
    str_p0_list = str_p0.split(",")

    str_p1 = dataRecord["p1"]
    str_p1_list = str_p1.split(",")

    str_p2 = dataRecord["p2"]
    str_p2_list = str_p2.split(",")

    str_p3 = dataRecord["p3"]
    str_p3_list = str_p3.split(",")

    str_p4 = dataRecord["p4"]
    str_p4_list = str_p4.split(",")

    p0 = Point(float(str_p0_list[0][1:]), float(str_p0_list[1][:-1]))
    p1 = Point(float(str_p1_list[0][1:]), float(str_p1_list[1][:-1]))
    p2 = Point(float(str_p2_list[0][1:]), float(str_p2_list[1][:-1]))
    p3 = Point(float(str_p3_list[0][1:]), float(str_p3_list[1][:-1]))
    p4 = Point(float(str_p4_list[0][1:]), float(str_p4_list[1][:-1]))

    if segmentsIntersect(Segment(p1, p2), Segment(p3, p4)) != int(dataRecord["p1p2 intersects p3p4"]):
        print("\nin %d record, the relationship between p1p2 and p3p4 is wrong!" % (dict_reader.line_num - 1))
        continue

    if pointInSegment(p0, Segment(p1, p2)) != int(dataRecord["p0 in p1p2(segment)"]):
        print("\nin %d record, the relationship between p0 and p1p2(s) is wrong!" % (dict_reader.line_num - 1))
        continue

    if pointInLine(p0, Line(p1, p2)) != int(dataRecord["p0 in p1p2(line)"]):
        print("\nin %d record, the relationship between p0 and p1p2(l) is wrong!" % (dict_reader.line_num - 1))
        continue

    print("\nthe %d record passes the test\n" % (dict_reader.line_num - 1))

csvFile.close()


print("point line test end!")