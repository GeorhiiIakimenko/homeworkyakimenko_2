class Point:
    x_coord = 0
    y_coord = 0

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x_coord = x
            self.y_coord = y
        else:
            raise TypeError("Coordinates must be of type int or float.")

    def __str__(self):
        return f'Point {self.x_coord} {self.y_coord}'

    def __getitem__(self, item):
        print(f'__getitem__ {item}')
        if item == 0:
            return self.x_coord
        elif item == 1:
            return self.y_coord
        else:
            raise TypeError

    def __setitem__(self, item, value):
        print(f'__setitem__ {item}, {value}')
        if item == 0:
            self.x_coord = value
        elif item == 1:
            self.y_coord = value
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x_coord == other.x_coord and self.y_coord == other.y_coord
        else:
            return False

    def distance(self, other_point):
        dx = self.x_coord - other_point.x_coord
        dy = self.y_coord - other_point.y_coord
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance


class Line:
    begin_point = None
    end_point = None

    def __init__(self, begin, end):
        if isinstance(begin, Point) and isinstance(end, Point):
            self.begin_point = begin
            self.end_point = end
        else:
            raise TypeError("Begin and end points must be instances of the Point class.")

    def __str__(self):
        return f'Line from [{self.begin_point}] to [{self.end_point}]'

    def length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord

        return (k1 ** 2 + k2 ** 2) ** 0.5

    def __len__(self):
        """ len(obj) """
        return 2

    def __contains__(self, item):
        """ a in b """
        print('__contains__', item)
        return self.begin_point == item or self.end_point == item


p1 = Point(3, 7)
p2 = Point(1, 2)

print(p1[0])
print(p1[1])

p1[1] = 100

print(p1)

line = Line(p1, p2)

print(p2 in line)
print(Point(0, 0) in line)


class Triangle:
    def __init__(self, point1, point2, point3):
        self._points = []
        for point in [point1, point2, point3]:
            if not isinstance(point, Point):
                raise TypeError("Triangle points must be instances of the Point class.")
            self._points.append(point)

    def __str__(self):
        return f'Triangle [{self._points[0]}], [{self._points[1]}], [{self._points[2]}]'

    @property
    def points(self):
        return iter(self._points)

    def area(self):
        # Lengths of sides of the triangle
        side1 = self._points[0].distance(self._points[1])
        side2 = self._points[1].distance(self._points[2])
        side3 = self._points[2].distance(self._points[0])

        # Semi-perimeter of the triangle
        semi_perimeter = (side1 + side2 + side3) / 2

        # Area calculation using Heron's formula
        area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5

        return area

