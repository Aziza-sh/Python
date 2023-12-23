import math
class vect:
    def __init__(self, coords):
        self.coords = coords 
        self.dim = len(coords)

        def __add__(self,other):
            if insinstance(other, vect) and self.dim:
                return vect(list(map(lambda x,y: x*y, self.coords, other.coords)))
            else:
                return vect([i*other for i in self.coords])
        def __sub__(self, other):
            pass
        def __rmul__(self,other):
            pass
        def __str__(self, other):
            pass
        def norm(self):
            return math.sqrt(self.self)
print(vect)