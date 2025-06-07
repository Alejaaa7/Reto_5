# Shape.py

class Shape:
    def _init__(self):
        self.is_regular = None
        self.vertices = []
        self.edges = []
        self.inner_angles = []

    def compute_area(self):
        raise NotImplementedError("Subclasses must contain compute_area()")
    
    def compute_perimeter(self):
        raise NotImplementedError("Subclasses must contain compute_perimenter()")
    
    def compute_inner_angles(self):
        raise NotImplementedError("Subclasses must contain compute_inner_angles()")
    
    def check_if_is_regular(self):
        if not self.edges or not self.inner_angles:
            return False
        if all(i == self.edges[0].length for i in self.edges) and \
            all(i == self.inner_angles[0] for i in self.inner_angles):
            return True
        else:
            return False