def permutations_state_space_tree(values):
    result = []  # persistent state

    def generate_tree(path, remaining):
        if not remaining:
            result.append(
                path[:]
            )  # shallow copy of the list (otherwise it would be changed by bactracking call)

        for index, value in enumerate(remaining):
            path.append(value)
            generate_tree(
                path, remaining[:index] + remaining[index + 1 :]
            )  # remove the current value from remaining for next choice
            path.pop()

        return result

    return generate_tree([], values)


if __name__ == "__main__":
    values = [1, 2]
    tree = permutations_state_space_tree(values)
    for value in tree:
        print(f"{value}")
