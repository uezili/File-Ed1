class StaticStack:
    def __init__(self, maximo):
        self.date = [None] * maximo
        self.size = 0
        self.max = maximo

    def stackSize(self):
        return self.size

    def __del__(self):
        return 0

    def stackFull(self):
        if self.size == self.max:
            return True
        return False

    def insertElement(self, element):
        if self.size == self.max:
            return False
        self.date[self.size] = element
        self.size += 1
        return self.date

    def removeElement(self):
        if self.date is None:
            return False
        self.size -= 1

    def topAccess(self):
        if self.size == 0 or self.date is None:
            return False
        return self.date[self.size - 1]

    def reverseStack(self):
        if self.date is None:
            return False
        stack = StaticStack(self.max)
        for i in range(self.size, -1, -1):
            stack.insertElement(self.date[i - 1])
        return stack.date

    def similarStack(self, stack):
        if stack.size != self.size:
            return "Não"
        equalElements = 0
        for i in range(0, self.size):
            if self.date[i] == stack.date[i]:
                equalElements += 1
        if equalElements == self.size:
            return "Sim"
        return "Não"

    def validEquation(self, equation=None):
        stack = StaticStack(20)
        for i in equation:
            if i == '(':
                stack.insertElement(i)
            elif i == ')':
                if stack.size > 0:
                    stack.size += 1
                stack.removeElement()
        if stack.size == 0:
            return "Correct equation!"
        return "Equation error!"
