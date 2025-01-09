class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def tree_levels_traversal(self) -> int:
        queue = [self]
        result = []
        level = []
        while queue:
            level = []
            for _ in range(len(queue)):
                current_node = queue.pop(0)
                level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(level)

        return result

    # Key difference between max height and max depth is what is taken into account while looking for the longues path
    # In max height edges are taken into account and in max depth is't the node.
    # NOTE : edges = nodes - 1
    def tree_height(self) -> int:
        queue = [self]
        tree_height = 0

        while queue:
            tree_height += 1

            for _ in range(len(queue)):
                current_node = queue.pop()
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return tree_height - 1  # because there are node-1 edges in a tree


if __name__ == "__main__":
    tree = Node(5)
    tree.left = Node(4)
    tree.right = Node(6)
    tree.left.left = Node(3)
    tree.left.right = Node(8)
    print(tree.tree_levels_traversal())
    print(tree.tree_height())
