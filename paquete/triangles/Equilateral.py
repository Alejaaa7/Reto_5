from ..shape.Point import Point
from ..shape.Line import Line
from ..shape.Shape import Shape
from ..triangles.Triangles import Triangles

class Equilateral(Triangles):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super()._init__(point1, point2, point3)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        if not self.if_is_equilateral:
            return ValueError("This points do not form an equilateral triangle.")
    
    def if_is_equilateral(self):
        return self.edges[0].lenght == self.edges[1].lenght \
                and self.edges[1].lenght == self.edges[2].lenght \
                and self.edges[2].lenght == self.edges[0].lenght