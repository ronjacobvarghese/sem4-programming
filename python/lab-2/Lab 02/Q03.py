class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.next

    def display_rev(self):
        if self.head is None:
            print("Linked list is empty!!")
        else:
            print()
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.prev

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def add_after(self, data, x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Node is not present")
            else:
                new_node = Node(data)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Node is not present")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.head = new_node
                n.prev = new_node

    def del_begin(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            self.head = None
            print("Only one node. Deleted!!")
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_end(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            self.head = None
            print("Only one node. Deleted!!!")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None

    def del_value(self, x):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            if x == self.head.data:
                self.head = None
            else:
                print("X is not present in LL")
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head
        while n.next is not None:
            if x == n.data:
                break
            n = n.next
        if n.next is not None:
            n.next.prev = n.prev
            n.prev.next = n.next
        else:
            if n.data == x:
                n.prev.next = None


a = DLL()
a.insert_empty(12)
a.add_begin(13)
a.add_end(14)
a.add_after(15,13)
a.add_before(120,14)
a.display()
a.display_rev()
a.del_begin()
a.del_end()
a.del_value(14)
print()
a.display()
