# Square.py

from ..shape.Point import Point
from ..shape.Line import Line
from ..shape.Shape import Shape

from ..rectangle.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, point1: Point, point2: Point, point3: Point, point4: Point):
        super().__init__(point1, point2, point3, point4)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        if not self.if_is_a_square:
            raise ValueError("The points do not form a square.")
    
    def if_is_a_square(self):
        if all(i == self.edges[0].length for i in self.edges):
            return True
        else:
            return False