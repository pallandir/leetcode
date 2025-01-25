def parenthesis_state_space_tree(n):
    result = []

    # In this function backtracking is managed by the immutability of the string and the fact that at each recursion a new string is created.
    def generate_parenthesis(current_string, opened, closed):
        if len(current_string) == 2 * n:
            result.append(current_string)
            return

        if opened < n:
            generate_parenthesis(current_string + "(", opened + 1, closed)
        if closed < opened:
            generate_parenthesis(current_string + ")", opened, closed + 1)

    generate_parenthesis("", 0, 0)
    return result


def generate_state_space_tree_2(n):
    result = []

    # Same result as the previous function but using a mutable data structure that forces visible backtracking (path.pop())
    def generate_parenthesis(path, opened, closed):
        if len(path) == 2 * n:
            result.append("".join(path))

        if opened < n:
            path.append("(")
            generate_parenthesis(path, opened + 1, closed)
            path.pop()

        if closed < opened:
            path.append(")")
            generate_parenthesis(path, opened, closed + 1)
            path.pop()

    generate_parenthesis([], 0, 0)
    return result


if __name__ == "__main__":
    print(parenthesis_state_space_tree(3))
    print(generate_state_space_tree_2(3))
