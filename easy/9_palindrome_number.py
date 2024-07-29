def palindrome_number(x):
    temp = x
    reversed = 0

    while temp > 0:
        digit = temp % 10
        reversed = reversed * 10 + digit
        temp = temp // 10
    return reversed == x


if __name__ == "__main__":
    print(palindrome_number(121))
