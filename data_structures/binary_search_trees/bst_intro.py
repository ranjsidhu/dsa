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

    def initialise_tree(self):
        self.insert(47)
        self.insert(21)
        self.insert(76)
        self.insert(18)
        self.insert(27)
        self.insert(52)
        self.insert(82)
        self.print_tree()

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

    def bfs(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results

    def dfs_preorder(self):
        current_node = self.root
        results = []

        return None


bst = BinarySearchTree()
bst.initialise_tree()
print("----------- Result -----------")
print(bst.bfs())
