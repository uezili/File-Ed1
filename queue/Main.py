from queue import Queue

N = int(input())
queue = Queue(5)
elem = "15243".split()
for i in range(N):
    queue.insertElement(elem[i])
queue.ordenar()
