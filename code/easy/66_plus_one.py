def plus_one(digits):
    number = int("".join(map(str, digits))) + 1
    return list(map(int, str(number)))


if __name__ == "__main__":
    print(plus_one([1, 2, 3]))
