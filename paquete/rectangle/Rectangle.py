# Rectangle.py

from ..shape.Point import Point
from ..shape.Line import Line
from ..shape.Shape import Shape


class Rectangle(Shape):
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point):
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        self.vertices = [point1, point2, point3, point4]
        self.edges = [Line(point1, point2),
                      Line(point2, point4),
                      Line(point4, point3),
                      Line(point3, point1)]
        self.inner_angles = self.compute_inner_angles
        self.is_regular = self.check_if_is_regular()

    def compute_area(self):
        return self.edges[0].length * self.edges[1].length
    
    def compute_perimeter(self):
        return self.edges[0].length + self.edges[1].length \
                + self.edges[2].length + self.edges[3].length
    
    def compute_inner_angles(self):
        return [90, 90, 90, 90]