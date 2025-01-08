def word_patterm(pattern, s):
    s = s.split(" ")
    return [pattern.index(char) for char in pattern] == [s.index(word) for word in s]


if __name__ == "__main__":
    print(word_patterm("abba", "dog cat cat dog"))  # true
    print(word_patterm("abba", "dog cat cat fish"))  # false
    print(word_patterm("aaaa", "dog cat cat dog"))  # false
    print(word_patterm("aaaa", "cat cat cat cat"))  # true
    print(word_patterm("abba", "cat cat cat cat"))  # false
