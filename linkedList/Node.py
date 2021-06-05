class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)
