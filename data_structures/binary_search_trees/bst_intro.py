class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        current = self.root
        while current is not None:
            print(f"in while loop and current is: {current.value}")
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            if prefix == "":
                node = self.root
            else:
                return

        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            self.print_tree(node.right, new_prefix, False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.print_tree(node.left, new_prefix, True)


bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)
bst.print_tree()
print("----------- Result -----------")
print(bst.contains(17))
