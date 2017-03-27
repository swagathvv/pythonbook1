import math

class Point(object):

first_point = Point()
second_point = Point()

first_point.x = 2.0
first_point.y = 4.0

second_point.x = 10.0
second_point.y = 15.0

def distance_between_points(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

print distance_between_points(first_point, second_point)
