class Node:
    def __init__(self, value, left=None, middle=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        self.middle = middle


def ternary_tree_path(root, path, res):
    if root is None:
        return
    path.append(str(root.val))
    if not root.left and not root.middle and not root.right:
        res.append("->".join(path))
    if root.left:
        ternary_tree_path(root.left, path, res)
    if root.middle:
        ternary_tree_path(root.middle, path, res)
    if root.right:
        ternary_tree_path(root.right, path, res)
    path.pop()


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.middle = Node(3)
    tree.right = Node(4)
    tree.left.left = Node(5)
    res = []
    ternary_tree_path(tree, [], res)
    print(res)
