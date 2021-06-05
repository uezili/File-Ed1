class Cube:
    def __init__(self, arrest=None):
        self.arr = arrest

    def createCube(self,x):
        c = Cube(x)
        return c

    def cubeArea(self, a):
        area = 6 * (a.arr ** 2)
        return area

    def cubeVolume(self, v):
        vol = v.arr**3
        return vol
    
    def cubeSide(self, s):
        side = s.arr * s.arr
        return side

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.arr}'
