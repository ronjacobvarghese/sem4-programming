class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class CircularList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " --> ", end="")
                n = n.ref
                if n == self.head:
                    break

    def add_begin(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.ref = self.head

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.ref = self.head
        elif self.head.ref is self.head:
            self.head.ref = new_node
            new_node.ref = self.head
        else:
            n = self.head
            while n.ref is not self.head:
                n = n.ref
            n.ref = new_node
            new_node.ref = self.head

    def after_node(self, data, x):
        n = self.head
        while n.ref != self.head:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not self.head:
                n = n.ref
            n.ref = self.head

    def delete_value(self, x):
        if self.head is None:
            print("LL is empty")
            return
        elif x == self.head.data:
            self.head = self.head.ref
        n = self.head
        while n.ref is not self.head:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is self.head:
            print("Node is not present!")
        else:
            n.ref = n.ref.ref

    def loop(self):
        if self.head is None:
            print("No loop. LL is empty!!")
        elif self.head.ref == self.head.data:
            print("Loop found")
        else:
            n = self.head
            while n.ref is not self.head:
                if n.ref.ref is self.head:
                    print("Loop found")
                    break
                else:
                    n = n.ref


a = CircularList()
a.add_begin(4)
a.after_node(6, 4)
a.display()
a.add_end(8)
a.add_end(10)
a.display()
a.loop()
