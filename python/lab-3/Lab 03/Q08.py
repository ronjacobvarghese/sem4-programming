class Queue:
    def __init__(node):
        node.data = []

    def Empty(node):
        return node.data == []

    def enQueue(node, data):
        node.data.insert(0, data)

    def deQueue(node):
        return node.data.pop()


def Reverse():
    if(Q.Empty()):
        return
    temp = Q.data[-1]
    Q.deQueue()
    Reverse()
    Q.enQueue(temp)


Q = Queue()
Q.enQueue(10)
Q.enQueue(8)
Q.enQueue(6)
Q.enQueue(4)
Q.enQueue(2)
print(Q.data)
Reverse()
print(Q.data)
