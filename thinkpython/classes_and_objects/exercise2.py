class Point(object):

class Rectangle(object):

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print box.corner.x
print box.corner.y

move_rectangle(box, 3.0, 3.0)

print box.corner.x
print box.corner.y
