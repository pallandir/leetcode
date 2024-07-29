def valid_parenthesis(s):
    pair = {"]": "[", ")": "(", "}": "{"}
    stack = []

    for char in s:
        if char in ("[", "(", "{"):
            stack.append(char)

        elif len(stack) > 0 and char in ("]", ")", "}") and pair[char] in stack[-1]:
            stack.pop()

        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    right = "(){}[]"
    wrong = "{}{()[]"
    wrong = "(]"
    wrong = "({{{{}}}))"
    print(valid_parenthesis(right))
    print(valid_parenthesis(wrong))
