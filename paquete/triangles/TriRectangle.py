# acabo de notar que en la anterior entrega me faltó el triángulo rectángulo :(
# TriRectangle.py

from ..shape.Point import Point
from ..shape.Line import Line
from ..shape.Shape import Shape

from ..triangles.Triangles import Triangles

class TriRectangle(Triangles):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__(point1, point2, point3)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        if not self.if_is_trirectangle:
            raise ValueError("This points do not form a right triangle.")
        
    def if_is_trirectangle(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length

        return a == (b ** 2 + c ** 2) ** 0.5 \
            or b == (a ** 2 + c ** 2) ** 0.5 \
            or c == (b ** 2 + a ** 2) ** 0.5