def first_occurence(s, t):
    if not s or not t:
        return False

    if len(t) != len(s):
        return False

    return [s.index(char) for char in s] == [t.index(char) for char in t]


def first_occurence2(s, t):
    return [*map(s.index, s)] == [*map(t.index, t)]


if __name__ == "__main__":
    print(first_occurence2("egg", "add"))
    print(first_occurence2("foo", "bar"))
    print(first_occurence2("paper", "title"))
    print(first_occurence2("bbbaaaba", "aaabbbba"))
