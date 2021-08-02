#  Binary tree depth
count: int = 0


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

    def search(self, val):
        if self.data == val:
            return

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)


def depth_node(root: BinarySearchTreeNode, data, level):
    if root is None:
        return 0
    if root.data == data:
        return level
    left_level = depth_node(root.left, data, level + 1)
    if left_level != 0:
        return left_level
    right_level = depth_node(root.right, data, level + 1)
    return right_level


def build_tree(elements) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 26, 9, 23, 18, 34]
    numbers_tree = build_tree(elements=numbers)
    print(depth_node(numbers_tree, 18, 1))
