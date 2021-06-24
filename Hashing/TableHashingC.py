class ItemHashing:
    def __init__(self, value, key):
        self.value = value
        self.key = key


class TableHashing:

    def __init__(self, maximum):
        self.size = maximum
        self.table = [None for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        if type(key) is str:
            mult = 1
            hv = 0
            for ch in key:
                hv += mult * ord(ch)
            return hv % self.size
        return key % self.size

    def insert(self, value, key=None):
        if key is None:
            key = value
        index = self._hash(key)
        element = ItemHashing(value, key)
        for i in range(self.size):
            if self.table[index] is None:
                self.table[index] = element
                self.count += 1
                print(f"Item insert in index: {index}")
                break
            index += 1
            if index == self.size:
                index = 0
            if self.size == self.count:
                raise ValueError("Table is full!")

    def search(self, key):
        calcH = self._hash(key)
        for i in range(self.size):
            if self.table[calcH].key == key:
                print(f'{self.table[calcH].value},\n{self.table[calcH].key},\nposition table: {calcH}')
                break
            if calcH == self.size:
                calcH = 0
            calcH = calcH + 1
