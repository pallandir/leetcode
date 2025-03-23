class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display_tree(self):
        queue = [self]
        level = []
        tree = []

        while queue:
            level = []
            for _ in range(len(queue)):
                current_node = queue.pop(0)
                level.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            tree.append(level)
        print(tree)


def invert_binary_tree(root):
    if root:
        root.left, root.right = (
            invert_binary_tree(root.right),
            invert_binary_tree(root.left),
        )
    return root


if __name__ == "__main__":
    tree = Node(5)
    tree.left = Node(3)
    tree.right = Node(4)
    tree.left.left = Node(2)
    tree.display_tree()
    new_tree = invert_binary_tree(tree)
    new_tree.display_tree()
