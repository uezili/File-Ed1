from NodeD import NodeD


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


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


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def sizeList(self):
        return self.size

    def emptyList(self):
        if self.size == 0:
            return True
        return False

    def insertFistList(self, element):
        node = NodeD(element)
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def insertEndList(self, element):
        if self.head is None:
            node = NodeD(element)
            self.head = node
            self.size += 1
            return node.data
        point = self.head
        while point.next is not None:
            point = point.next
        node = NodeD(element)
        point.next = node
        node.prev = point
        self.size += 1

    def getNode(self, index):
        point = self.head
        for i in range(index):
            if point:
                point = point.next
            else:
                raise IndexError("Index out of list")
        return point

    def insertElementTheMiddle(self, index, element):
        node = NodeD(element)
        if index == 0:
            self.insertFistList(element)
        elif index == self.size:
            self.insertEndList(element)
        elif index > self.size:
            raise IndexError("Index out of list")
        else:
            point = self.getNode(index - 1)
            node.next = point.next
            point.next.prev = node
            point.next = node
            node.prev = point
            self.size = self.size + 1

    def removeFistElement(self):
        if self.emptyList():
            raise IndexError("the list is empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def removeEndElement(self):
        if self.emptyList():
            raise IndexError("the list is empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.anterior
            self.tail.next = None
        self.size = self.size - 1

    def index(self, element):
        point = self.head
        indexElement = 0
        while point:
            if point.date == element:
                return indexElement
            point = point.next
            indexElement += 1
        raise ValueError(f"{element} it's not on the list")

    def __repr__(self):
        if self.size > 0:
            represent = "<-"
            obj = self.head
            r = 0
            while obj:
                if r == 0:
                    represent = represent + str(obj.dado)
                if (obj is not None) and (r != 0):
                    represent = represent + "<->" + str(obj.dado)
                obj = obj.proximo
                if obj is None:
                    represent = represent + "->"
                    break
                r = 1
            return represent
        return "Empty List"

    def __str__(self):
        return self.__repr__()

    def listprint(self, node):
        for i in range(self.size, 0, -1):
            print(node.data, end=' -> '),
            last = node
            node = node.next

    def impaPar(self):
        listPar = LinkedList()
        listImpa = LinkedList()
        point = self.head
        while point:
            if point.date % 2 == 0:
                listPar.fistInsertElement(point.data)
            else:
                listImpa.fistInsertElement(self.getNode(point.data))
            point = point.next
        return listImpa, listPar


