# Isosceles.py

from ..shape.Point import Point
from ..shape.Line import Line
from ..shape.Shape import Shape
from ..triangles.Triangles import Triangles

class Isosceles(Triangles):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__(point1, point2, point3)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        if not self.if_is_isosceles:
            return ValueError("This points do not form an isosceles triangle.")

    def if_is_isosceles(self):
        return self.edges[0].length == self.edges[1].length \
                or self.edges[1].length == self.edges[2].length\
                or self.edges[2].length == self.edges[0].length