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
        return (key & 0x7FFFFFF) % self.size

    def linearProbing(self, key, const):
        return ((key + const) & 0x7FFFFFFF) % self.size

    def insert(self, value):
        if self.size == self.count:
            raise ValueError("Table is full!")
        index = int(self._hash(value))
        for i in range(self.count):
            newIndex = self.linearProbing(index, i)
            if self.table[newIndex] is None:
                element = ItemHashing(value, newIndex)
                self.table[newIndex] = element
                self.count += 1
                print(f"Item insert in index: {newIndex}")
                break

    def search(self, value):
        key = int(value)
        index = self._hash(key)
        for i in range(self.count):
            newIndex = self.linearProbing(index, i)
            if self.table[newIndex]:
                if self.table[newIndex].value == value:
                    print(f'{self.table[i].value},\n{self.table[i].key},\nposition table: {i}')
                    return
        raise ValueError('Item not found')

    def sizeTible(self):
        return self.count

    def seeTable(self):
        for i in range(self.size):
            print(f'{self.table[i]}')
