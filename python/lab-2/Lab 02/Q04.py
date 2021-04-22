class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None

    def Display(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " --> ", end="")
                n = n.next
                if n == self.head:
                    break

    def add_begin(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = self.head

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        elif self.head.next is self.head:
            self.head.next = new_node
            new_node.next = self.head
        else:
            n = self.head
            while n.next is not self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head

    def after_node(self, data, x):
        n = self.head
        while n.next != self.head:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node not present in Linked List")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not self.head:
                n = n.next
            n.next = self.head

    def delete_value(self, x):
        if self.head is None:
            print("LL is empty")
            return
        elif x == self.head.data:
            self.head = self.head.next
        n = self.head
        while n.next is not self.head:
            if n.next.data == x:
                break
            n = n.next
        if n.next is self.head:
            print("Node is not present!")
        else:
            n.next = n.next.next


a = CircularList()
a.add_begin(14)
a.after_node(16, 14)
a.Display()
a.add_end(18)
a.add_end(10)
a.Display()
print()
a.delete_begin()
a.delete_value(16)
a.delete_end()
a.Display()
