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

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

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

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:  # node on left and right of node being deleted
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min
                )

        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

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
bst.r_insert(47)
bst.r_insert(21)
bst.r_insert(76)
bst.r_insert(18)
bst.r_insert(27)
bst.r_insert(52)
bst.r_insert(82)
bst.print_tree()
print("--------------------  Result  --------------------")
bst.delete_node(21)
bst.print_tree()
