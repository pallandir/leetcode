class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder_traversal(self):
        stack = []
        traversed = []
        current_node = self

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            traversed.append(current_node.val)
            current_node = current_node.right

        return traversed

    def rec_inorder_traversal(self):
        current = self
        traversed = []

        def rec_h_traverse(node):
            if not node:
                return

            rec_h_traverse(node.left)
            traversed.append(node.val)
            rec_h_traverse(node.right)

        rec_h_traverse(current)

        return traversed


if __name__ == "__main__":
    tree = Node(5)
    tree.left = Node(3)
    tree.right = Node(2)
    tree.left.left = Node(6)
    print(tree.inorder_traversal())
    print(tree.rec_inorder_traversal())
