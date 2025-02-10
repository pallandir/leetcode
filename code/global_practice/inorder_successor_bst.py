class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_successor(root, node):
    successor = None

    while root:
        if node.val < root.val:
            # the current root could be the right successor but one on the left could also be smaller and meet the condition
            successor = root
            root = root.left
        else:
            root = root.right
    return successor.val


if __name__ == "__main__":
    # in  a BST the node on the left is smaller than the root and the node on the right is bigger than the root
    tree = Node(20)
    tree.left = Node(10)
    tree.right = Node(30)
    tree.left.left = Node(8)
    tree.left.right = Node(15)

    print(inorder_successor(tree, Node(10)))
