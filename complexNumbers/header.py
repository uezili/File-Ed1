class ComplexNumber:
    def __init__(self, real=None, imaginary=None):
        self.rea = real
        self.img = imaginary

    @staticmethod
    def createComplexNumber(x, y):
        z = ComplexNumber(x, y)
        return z

    def __del__(self, *number):
        return 'Conteudo deletado'

    def multiplyingTwoComplexNumbers(self, x, y):
        nRea = x.rea * y.rea
        nImg = x.img * y.img
        return ComplexNumber(nRea, nImg)

    def conjugateNumber(self, num):
        reaNum = num.rea
        imgNum = num.img * -1
        return ComplexNumber(reaNum, imgNum)

    def divisionTwoComplexNumbers(self, x, y):
        reaNun = (x.rea * y.rea + x.img * y.img) / (y.rea ** 2 + y.img ** 2)
        imgNum = (y.rea * x.img - x.rea * y.img) / (y.rea ** 2 + y.img ** 2)
        diviNum = reaNun * imgNum
        return diviNum

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.img < 0:
            return f'{self.rea} - {abs(self.img)}i'
        return f'{self.rea} + {self.img}i'
