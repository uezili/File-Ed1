from Node import Node


class DynamicStack:
    def __init__(self):
        self.prox = None
        self.size = 0

    def sizeStack(self):
        return self.size

    def insertElement(self, element):
        node = Node(element)
        node.next = self.prox
        self.prox = node
        self.size += 1
        return node.data

    def removeElement(self):
        if self.size != 0:
            node = self.next
            self.next = self.next.next
            self.size -= 1
            return node.data
        return "There is no element in the stack!"

    def viewTopStack(self):
        if self.size != 0:
            return self.prox.data
        return "There is no element in the stack!"

    def __del__(self):
        return 0

    def __repr__(self):
        represent = ""
        pointer = self.prox
        while pointer:
            represent = represent + str(pointer.data) + "\n"
        return represent

    def __str__(self):
        return self.__repr__()
