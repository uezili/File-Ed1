from TableHashingC import TableHashing

table = TableHashing(100)

with open('5intens.txt'.swapcase(), 'r') as file:
    for i in file:
        table.insert(i)

table.seeTable()
