from Circle import *
from Rectangle import *
import csv

print("rectangle test begin...\n")
csvFile = open("GeoData_rect.csv", "r")
dict_reader = csv.DictReader(csvFile)

for dataRecord in dict_reader:

    # variable assignment

    str_p1 = dataRecord["p1"]
    str_p1_list = str_p1.split(",")

    str_p2 = dataRecord["p2"]
    str_p2_list = str_p2.split(",")

    str_p3 = dataRecord["p3"]
    str_p3_list = str_p3.split(",")

    str_pa = dataRecord["pa"]
    str_pa_list = str_pa.split(",")

    str_pb = dataRecord["pb"]
    str_pb_list = str_pb.split(",")

    str_p0 = dataRecord["p0"]
    str_p0_list = str_p0.split(",")

    p1 = Point(float(str_p1_list[0][1:]), float(str_p1_list[1][:-1]))
    p2 = Point(float(str_p2_list[0][1:]), float(str_p2_list[1][:-1]))
    p3 = Point(float(str_p3_list[0][1:]), float(str_p3_list[1][:-1]))
    pa = Point(float(str_pa_list[0][1:]), float(str_pa_list[1][:-1]))
    pb = Point(float(str_pb_list[0][1:]), float(str_pb_list[1][:-1]))
    p0 = Point(float(str_p0_list[0][1:]), float(str_p0_list[1][:-1]))

    cx = float(dataRecord["cx"])
    cy = float(dataRecord["cy"])
    radius = float(dataRecord["radius"])

    circle = Circle(Point(cx, cy), radius)
    rect = Rectangle(p1, p2, p3, Point(p3.x, p1.y))

    if pointInRectangle(p0, rect) != int(dataRecord["p0 in rect"]):
        print("\nin %d record, the relationship between p0 and rect is wrong!" % (dict_reader.line_num - 1))
        continue

    if segmentIntersectsRectangle(Segment(pa, pb), rect) != int(dataRecord["papb(segment) intersects rect"]):
        print("\nin %d record, the relationship between papb(s) and rect is wrong!" % (dict_reader.line_num - 1))
        continue

    if lineIntersectsRectangle(Line(pa, pb), rect) != int(dataRecord["papb(line) intersects rect"]):
        print("\nin %d record, the relationship between papb(l) and rect is wrong!" % (dict_reader.line_num - 1))
        continue

    if circleIntersectsRectangle(circle, rect) != int(dataRecord["circle intersects rect"]):
        print("\nin %d record, the relationship between circle and rect is wrong!" % (dict_reader.line_num - 1))
        continue

    print("\nthe %d record passes the test\n" % (dict_reader.line_num - 1))

csvFile.close()

print("rect test end")



