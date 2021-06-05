from Node import Node


class DynamicQueue:
    def __init__(self):
        self.fist = None
        self.last = None
        self.size = 0

    def queueSize(self):
        return self.size

    def queueFistElement(self):
        return self.fist

    def insertElement(self, element):
        node = Node(element)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.fist is None:
            self.fist = node
        self.size += 1
        return "Queue element insertion!"

    def removeElement(self):
        if self.fist is not None:
            element = self.fist.data
            self.fist = self.fist.next
            self.size -= 1
            return element
        return 'Queue is enable'

    def viwFistElement(self):
        if self.size is not None:
            element = self.fist.data
            return element
        return 'Queue is enable'

    def __repr__(self):
        if self.size is not None:
            r = ''
            pointer = self.fist
            while pointer:
                r = r + str(pointer.data) + ' '
                pointer = pointer.next
            return r
        return 'Queue is enable'

    def sunQueue(self):

    def __str__(self):
        return self.__repr__()
