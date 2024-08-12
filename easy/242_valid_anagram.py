def valid_palindrome(s, t):
    return {char: s.count(char) for char in set(s)} == {
        char: t.count(char) for char in set(t)
    }


if __name__ == "__main__":
    print(valid_palindrome("anagram", "nagaram"))
    print(valid_palindrome("rat", "car"))
