from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def fistInsertElement(self, element):
        node = Node(element)
        node.next = self.head
        self.head = node
        self.size += 1

    def insertElementTheMiddle(self, index, element):
        if index == 0:
            node = Node(element)
            node.next = self.head
            self.head = node
            self.size += 1
        else:
            point = self.head
            for i in range(index - 1):
                if point is not None:
                    point = point.next
                else:
                    raise IndexError('list index out of range')
            node = Node(element)
            node.next = point.next
            point.next = node
            self.size += 1

    def insertElementTheEnd(self, element):
        if self.head:
            point = self.head
            while point.next:
                point = point.next
            point.next = Node(element)
        else:
            self.head = Node(element)
        self.size = self.size + 1

    def removeElement(self, element):
        if self.head is None:
            raise ValueError(f'{element} is not list')
        elif self.head.data == element:
            self.head = self.head.data
            self.size -= 1
        else:
            previous = self.head
            point = self.head.next

            while point:
                if point.data == element:
                    previous.next = point.next
                    point.next = None
                previous = point
                point = point.next
            self.size -= 1
        raise ValueError(f'{element} is not list')

    def sizeList(self):
        return self.size

    def __repr__(self):
        return "[" + str(self.head) + "]"
