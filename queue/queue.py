class Queue:
    def __init__(self, maximum):
        self.max = maximum
        self.data = [None] * maximum
        self.fist = 0
        self.last = 0
        self.size = 0

    def viwFistElement(self):
        return self.data[self.fist]

    def queueSize(self):
        return self.size

    def queueFull(self):
        if self.size == self.max:
            return True
        return False

    def __del__(self):
        return 0

    def insertElement(self, element):
        if self.max == self.size:
            return False
        else:
            self.data[self.last] = element
            self.last = (self.last + 1) % self.max
            self.size += 1
        return self.data

    def removeElement(self):
        if self.size == 0:
            return False
        else:
            element = self.data[self.fist]
            self.data[self.fist] is None
            self.fist = (self.fist + 1) % self.max
        self.size -= 1
        return element

    def copyQueue(self):
        if self.data is None:
            return None
        queue = Queue(self.max)
        for i in range(self.max):
            queue.insertElement(self.data[i])
        return queue

    def concatenateQueue(self, queue1, queue2):
        if queue1 is None or queue2 is None:
            return None
        sizeMax = queue1.size + queue2.size
        queue = Queue(sizeMax)
        for i in range(queue1.size):
            queue.insertElement(queue1.data[i])
        for i in range(queue2.size):
            queue.insertElement(queue2.data[i])
        return queue

    def inverterOrder(self):
        if self.data is None:
            return None
        queue = Queue(self.max)
        for i in range(self.last, self.max):
            queue.insertElement(self.data[i])
        return queue.data

