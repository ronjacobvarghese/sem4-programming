class Tree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.parent = None
            self.data = data
            print("Node Created", self.data)

        def printNode(self):
            print("printing...", self.data)

        def insert(self, Nd):
            if Nd.data < self.data:
                if self.left is None:
                    self.left = Nd
                    Nd.parent = self
                else:
                    self.left.insert(Nd)
            else:
                if self.right is None:
                    self.right = Nd
                    Nd.parent = self
                else:
                    self.right.insert(Nd)

        def preorder_traverse(self):
            if self is not None:
                print(self.data,end = " ")
            if self.left is not None:
                self.left.preorder_traverse()
            if self.right is not None:
                self.right.preorder_traverse()
        def inorder_traverse(self):
            if self.left is not None:
                self.left.inorder_traverse()
            if self is not None:
                print(self.data,end = " ")
            if self.right is not None:
                self.right.inorder_traverse()

        def postorder_traverse(self):
            if self.left is not None:
                self.left.postorder_traverse()
            if self.right is not None:
                self.right.postorder_traverse()
            if self is not None:
                print(self.data,end = " ")
    def addRoot(self, dt):
        self.root = self.Node(dt)
        self.size = 1
        print("Root added")

    def isRoot(self, dt):
        if self.root.data == dt:
            print("Yes Root")
        else:
            print("No")

    def traverseNLR(self):
        print("Preorder Traversal")
        self.root.preorder_traverse()
        print()

    def traverseLRN(self):
        print("Postorder Traversal")
        self.root.postorder_traverse()
        print()

    def traverseLNR(self):
        print("In order Traversal")
        self.root.inorder_traverse()
        print()

    def buildTree(self):
        self.addRoot(4)
        n1 = self.Node(8)
        n2 = self.Node(7)
        n3 = self.Node(1)
        n4 = self.Node(6)
        n5 = self.Node(5)
        n6 = self.Node(2)
        n7 = self.Node(3)
        n8 = self.Node(9)
        n9 = self.Node(10)
        n10 = self.Node(11)
        self.root.insert(n1)
        self.root.insert(n2)
        self.root.insert(n3)
        self.root.insert(n4)
        self.root.insert(n5)
        self.root.insert(n6)
        self.root.insert(n7)
        self.root.insert(n8)
        self.root.insert(n9)
        self.root.insert(n10)
        
T = Tree()
T.buildTree()
T.traverseLNR()
    
