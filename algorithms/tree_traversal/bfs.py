# This is the standalone code
# see data_structures/binary_search_trees/bst_intro.py for the implementation


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
