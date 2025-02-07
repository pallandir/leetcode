class Node:
    def __init__(self, value, children=None):
        self.val = value
        self.children = children if children else []

    def display_tree(self):
        queue = [self]
        level = []
        tree = []

        while queue:
            level = []
            for _ in range(len(queue)):
                current_node = queue.pop(0)
                level.append(current_node.val)
                queue.extend(
                    current_node.children
                )  # becuase current_node.children is a list
            tree.append(level)
        return tree


def n_letters_state_space(chars_list, depth):
    def generate_tree(current_word, depth):
        if depth == 0:
            return Node(current_word)
        root = Node(current_word)

        for char in chars_list:
            child = generate_tree(current_word + char, depth - 1)
            root.children.append(child)
        return root

    return generate_tree("", depth)


if __name__ == "__main__":
    chars = ["a", "b"]
    depth = 3

    tree = n_letters_state_space(chars, depth)
    print(tree.display_tree())
