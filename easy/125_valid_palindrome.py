def valid_palindrome(s):
    s_format = "".join([char.lower() for char in s if char.isalnum()])
    return s_format == s_format[::-1]


if __name__ == "__main__":
    numbers: list = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]

    for s in numbers:
        print(valid_palindrome(s))
