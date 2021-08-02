class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add to left sub tree
            if self.left:
                self.left.add_child(data)  # next subtree.
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            # add to right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):

        elements = []
        # we first check the left sub trees
        if self.left:
            elements += self.left.in_order_traversal()

        # base node
        elements.append(self.data)

        # right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 26, 9, 23, 18, 34]
    numbers_tree = build_tree(elements=numbers)
