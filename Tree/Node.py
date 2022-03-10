class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)

    def print_node(self):
        if self is None:
            pass
        print("root: {}".format(self.val), end=" ")
        if self.left:
            print("left: {}".format(self.left.val), end=" ")
        if self.right:
            print("right: {}".format(self.right.val), end=" ")
        print("\n")
        if self.left:
            self.left.print_node()
        if self.right:
            self.right.print_node()


class BST:
    def __init__(self):
        self.root = None


if __name__ == '__main__':
    root = Node(10)
    root.insert(8)
    root.insert(15)
    root.insert(7)
    root.insert(9)
    root.insert(13)
    root.insert(4)
    root.print_node()


