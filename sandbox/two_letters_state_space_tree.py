class Node:
    def __init__(self, value, children=None):
        self.val = value
        self.children = children if children else []

    def display_tree(self, level=0):
        level = []
        res = []
        queue = [self]

        while queue:
            level = []
            for _ in range(len(queue)):
                current = queue.pop(0)
                level.append(current.val)
                queue.extend(current.children)
            res.append(level)

        print(res)


def state_space_tree(chars_list):
    def generate_tree(current_word, depth):
        if depth == 0:
            return Node(current_word)
        root = Node(current_word)

        for char in chars_list:
            child = generate_tree(current_word + char, depth - 1)
            root.children.append(child)

        return root

    return generate_tree("", len(chars_list))


if __name__ == "__main__":
    chars = ["a", "b"]
    tree = state_space_tree(chars)
    tree.display_tree()
