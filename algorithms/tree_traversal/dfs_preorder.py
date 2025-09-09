# This is the standalone code
# see data_structures/binary_search_trees/bst_intro.py for the implementation


def dfs_pre_order(self):
    results = []

    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return results
