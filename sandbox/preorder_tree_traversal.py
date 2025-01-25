class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root -> left -> right
def preorder_traversal(root):
    traversed = []
    stack = [root]

    while stack:
        current_node = stack.pop()
        traversed.append(current_node.val)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    return traversed


if __name__ == "__main__":
    tree = Node(5)
    tree.left = Node(3)
    tree.right = Node(2)
    tree.left.left = Node(6)
    print(preorder_traversal(tree))
