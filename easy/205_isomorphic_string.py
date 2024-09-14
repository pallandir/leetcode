def isomorphic_string2(s, t):
    if not s or not t:
        return False

    if len(t) != len(s):
        return False

    return [s.index(char) for char in s] == [t.index(char) for char in t]


def isomorphic_string(s, t):
    return [*map(s.index, s)] == [*map(t.index, t)]


if __name__ == "__main__":
    print(isomorphic_string("egg", "add"))
    print(isomorphic_string("foo", "bar"))
    print(isomorphic_string("paper", "title"))
    print(isomorphic_string("bbbaaaba", "aaabbbba"))
