# Triangles.py

from ..shape.Point import Point
from ..shape.Line import Line
from ..shape.Shape import Shape

from math import degrees, acos

class Triangles(Shape):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.vertices = [point1, point2, point3]
        self.edges = [Line(point1, point2),
                      Line(point2, point3),
                      Line(point3, point1)]
        self.inner_angles = self.compute_inner_angles()
        self.is_regular = self.check_if_is_regular()

    def compute_inner_angles(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        angle_A = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
        angle_B = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
        angle_C = degrees(acos((a ** 2 + b ** 2 - c ** 2 ) / (2 * a * b)))
        return [angle_A, angle_B, angle_C]
    
    def compute_area(self):
        semiperimeter = (self.edges[0].length + self.edges[1].length + \
                         self.edges[2].length) / 2
        area = (semiperimeter * (semiperimeter - self.edges[0].length) * \
                (semiperimeter - self.edges[1].length) *\
                (semiperimeter - self.edges[2].length)) ** 0.5
        return area
    
    def compute_perimeter(self):
        return self.edges[0].length + self.edges[1].length + self.edges[2].length
    
    