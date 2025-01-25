class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visible_tree(root):
    if not root:
        return []

    queue = [root]
    right_child = None
    result = []

    while queue:
        for _ in range(len(queue)):
            current_node = queue.pop(0)
            # The reason this works is because at the current iteration of the loop, we have all child of a same level
            # and the right most element will be pop last and will erase the previous value.
            right_child = current_node.val

            # If the goal is to print left visible tree then we can invert these push to the queue so the last item to be poped will be the
            # left most one
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(right_child)
    return result


if __name__ == "__main__":
    tree = Node(5)
    tree.left = Node(4)
    tree.right = Node(6)
    tree.left.left = Node(3)
    tree.left.right = Node(8)
    print(visible_tree(tree))
