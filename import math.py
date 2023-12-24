import math

class c_n:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def to_polar(self):
        m = math.hypot(self.re, self.im)

        if self.re > 0 and self.im > 0:
            a = math.atan(self.im/self.re) + math.pi
        elif self.re < 0 and self.im > 0:
            a = math.atan(self.im/self.re) - math.pi

        return m, a
    def __pow__(self, p):
        m, a = self.to_polar()

        return c_n(m**p*math.cos(p*a), m**p*math.sin(p*a))
    
    for i in range(n):
        roots.apend(c_n(m*math.cos((a + 2*math.pi)/n)), m*math.sin((a + 2*math.pi)/n))
        return roots
    
