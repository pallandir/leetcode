def happy_number(n):
    happy_number = False
    visited = []

    while n > 0:
        n = sum(int(digit) ** 2 for digit in str(n))
        if n in visited:
            break

        visited.append(n)

        if n == 1:
            happy_number = True
            break

    return happy_number


if __name__ == "__main__":
    print(happy_number(19))
    print(happy_number(2))
    print(happy_number(15))
