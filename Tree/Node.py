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

    def search(self, key):
        if self is None:
            print("root is empty")
            return False
        if key < self.val:
            if self.left:
                return self.left.search(key)
            else:
                return False
        elif key > self.val:
            if self.right:
                return self.right.search(key)
            else:
                return False
        else:
            return True


class BST:
    def __init__(self):
        self.root = None

    def create_bst(self, lst):
        if len(lst) == 0:
            print("List is empty")
            return
        if self.root is None:
            self.root = Node(lst[0])

        if len(lst) > 1:
            for val in lst[1:]:
                self.root.insert(val)

    def search_bst(self, key):
        return self.root.search(key)


if __name__ == '__main__':
    lst = [10, 8, 15, 7, 9, 13, 4]
    bst = BST()
    bst.create_bst(lst)
    bst.root.print_node()
    print(bst.search_bst(4))
    print(bst.search_bst(9))
    print(bst.search_bst(14))




