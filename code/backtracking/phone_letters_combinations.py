def combination_state_space(numbers):
    result = []
    phone_keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def generate_tree(path, remaining):
        if not remaining:
            result.append("".join(path))
            return

        current_number = remaining[0]
        letters = phone_keyboard.get(current_number, "")
        for letter in letters:
            path.append(letter)
            generate_tree(path, remaining[1:])
            path.pop()

    generate_tree([], numbers)
    return result


if __name__ == "__main__":
    numbers = "23"
    tree = combination_state_space(numbers)
    for value in tree:
        print(value)
