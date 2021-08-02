class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__ (self):
        self.head = Node ("head")
        self.size = 0

    def __str__ (self):
        cur = self.head.next
        out = ""
        while cur:
            out += str (cur.value) + "->"
            cur = cur.next
        return out [:-3]

    def getSize (self):
        return self.size

    def isEmpty (self):
        return self.size == 0

    def peek (self):

        if self.isEmpty ():
            raise Exception ("Peeking from an empty stack")
        return self.head.next.value

    def push (self, value):
        node = Node (value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop (self):
        if self.isEmpty ():
            raise Exception ("Popping from an empty stack")
        rem = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return rem.value

    def insertAtBottom (self, item):
        if self.isEmpty ():
            self.push (item)
        else:
            temp = self.pop ()
            self.insertAtBottom (item)
            self.push (temp)

    def reverse (self):
        if not self.isEmpty ():
            temp = self.pop ()
            self.reverse ()
            self.insertAtBottom(temp)


if __name__ == "__main__":
    stack = Stack ()
    for i in range (1, 11):
        stack.push (i)
    print (f"Stack: {stack}")

    for _ in range (1, 6):
        remove = stack.pop ()
        print (f"Pop: {remove}")
    print (f"Stack: {stack}")
    stack.reverse()
    print("Stack after reverse")
    print (f"Stack: {stack}")

