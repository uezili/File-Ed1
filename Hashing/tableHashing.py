class ItemHash:
    def __init__(self, value, key):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, maximum):
        self.size = maximum
        self.slots = [None for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        if type(key) is str:
            mult = 1
            hv = 0
            for ch in key:
                hv += mult * ord(ch)
            return hv % self.size
        return key % self.size

    def insert(self, value, key):
        index = self._hash(key)
        element = ItemHash(value, key)
        if self.slots[index] is None:
            self.slots[index] = element
            self.count += 1
            print("item insert")
            return
        else:
            raise ValueError("Error, collision!")

    def seeTable(self):
        return self.slots

    def search(self, key):
        calc = self._hash(key)
        if self.slots[calc] is not None:
            print(f'{self.slots[calc].value},\n{self.slots[calc].key},\nposition table: {calc}')
            return
        raise ValueError("Item not found.")

    def __del__(self):
        return 0
