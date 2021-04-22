class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.ref
            print()

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def after_node(self, data, x):
        n = self.head
        while n is not None:
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
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_value(self, x):
        if self.head is None:
            print("LL is empty")
            return
        elif x == self.head.data:
            self.head = self.head.ref
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present!")
        else:
            n.ref = n.ref.ref

    def rem_dup(self):
        current = self.head
        temp = self.head
        while current is not None:
            while temp.ref is not None:
                if temp.ref.data == current.data:
                    temp.ref = temp.ref.ref
                else:
                    temp = temp.ref
            temp = current.ref
            current = current.ref


a = LinkedList()
a.add_begin(12)
a.after_node(16, 12)
a.after_node(18, 16)
a.add_end(14)
a.add_end(14)
a.display()
a.rem_dup()
a.display()
