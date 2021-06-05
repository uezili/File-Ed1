from Node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def sizeList(self):
        return self.size

    def insertFistList(self, element):
        node = Node(data=element)
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node
        self.head = node
        self.size += 1
        return node.data

    def insertEndList(self, element):
        node = Node(data=element)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.size += 1
        return node.data
    #def insertBetweenElements(self, element, index):

