from tableHashing import HashTable

table = HashTable(7)
table.insert('wesley', 1998)
table.insert(1998, 'wesley')
table.seeTable()
table.search('wesley')
table.search(1998)
