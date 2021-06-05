class StaticList:
    def __init__(self, maxSize):
        self.max = maxSize
        self.list = [None] * maxSize
        self.size = 0

    def sizeList(self):
        if self.size == 0:
            return "List is empty."
        return self.size

    def viewList(self):
        return self.list

    def __del__(self):
        return "deleted list."

    def fullList(self):
        if self.list is None:
            return 'invalid list!'
        if self.size == self.max:
            return True
        return False

    # noinspection PyUnresolvedReferences
    def firstElementInsert(self, element):
        if self.list is None:
            self.list[0] = element
            self.size += 1
            return self.list
        elif self.size == self.max:
            return "Full list"
        else:
            for i in range(self.size, 0, -1):
                self.list[i] = self.list[i - 1]
            self.list[0] = element
        self.size += 1
        return self.list

    def insertElementTheEnd(self, element):
        if self.list is None:
            return 'invalid list!'
        if self.size == self.max:
            return 'Full list!'
        self.list[self.size] = element
        self.size += 1
        return self.list

    def insertElementTheMiddle(self, element, index):
        if self.list is None:
            return "invalid list!"
        elif self.size == self.max:
            return 0
        else:
            for i in range(self.size, index, -1):
                self.list[i] = self.list[i - 1]
            self.list[index] = element
            self.size += 1
            return self.list

    def checkElement(self, element):
        if self.size == 0:
            return "list does not contain elements"
        for i in range(0, self.size):
            if element == self.list[i]:
                return f'element in the index: {i}'
        return "element does not exist!"

    def removeElement(self, index):
        if index > self.size:
            return "index does not exist!"
        if self.size == 0:
            return "list does not contain elements!"
        for i in range(index, self.size):
            self.list[i] = self.list[i + 1]
        self.size -= 1
        return self.list
