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

    def delete(self, key):
        """
        1. if the key has no children (leaf node), just delete it directly
        2. if the key has one child, let this child replace it
        3. if the key has 2 children, let the maximum of left tree of it replace it,
        i.e. the most right node of left child
        """
        if self is None:
            print("root is None")
            return
        if key < self.val:
            if self.left:
                self.left = self.left.delete(key)
            else:
                print("not found the key: {}".format(key))
        elif key > self.val:
            if self.right:
                self.right = self.right.delete(key)
            else:
                print("not fount the key: {}".format(key))
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                node = self.left
                while node.right:
                    node = node.right
                self.val = node.val
                self.left = self.left.delete(node.val)
        return self

    def pre_order(self):
        if self is None:
            print("root is None")
        print(self.val, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self is None:
            print("root is None")
        if self.left:
            self.left.in_order()
        print(self.val, end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self is None:
            print("root is None")
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.val, end=" ")


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

    def delete_bst(self, key):
        return self.root.delete(key)

    def print_bst(self):
        self.root.print_node()

    def bst_pre_order(self):
        self.root.pre_order()

    def bst_in_order(self):
        self.root.in_order()

    def bst_post_order(self):
        self.root.post_order()


if __name__ == '__main__':
    lst = [10, 8, 15, 6, 9, 13, 4, 7]
    bst = BST()
    bst.create_bst(lst)
    # bst.root.print_node()
    # print(bst.search_bst(4))
    # print(bst.search_bst(9))
    # print(bst.search_bst(14))
    # bst.print_bst()
    # bst.delete_bst(13)
    bst.root.pre_order()
    bst.root.in_order()
    bst.root.post_order()
    print("\n")
    bst.bst_pre_order()
    bst.bst_in_order()
    bst.bst_post_order()






