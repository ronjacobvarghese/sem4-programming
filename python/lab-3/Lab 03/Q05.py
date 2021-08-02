class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue Is Full\n")
        elif (self.front == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if (self.front == -1):
            print("Queue Is Empty\n")
        elif (self.front == self.rear):
            value = self.queue[self.front]
            self.front = self.rear = -1
            return value
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return value

    def print(self):
        if (self.front == -1):
            print("Queue Empty")
        elif (self.rear > self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            print()


q = CircularQueue(5)
print("\nEnqueue:")
q.enqueue(12)
q.enqueue(24)
q.enqueue(26)
q.enqueue(28)
q.enqueue(10)
q.print()
q.dequeue()
q.dequeue()
print("\nAfter Dequeue:")
q.print()
print("\nEnqueue Again:")
q.enqueue(121)
q.enqueue(142)
q.print()
