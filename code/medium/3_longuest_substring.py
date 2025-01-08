def longuest_substr(s: str):
    s_i, s_j = 0, 0
    visited_char = set()
    longuest_str = 0

    for char in s:
        while char in visited_char:
            visited_char.remove(s[s_i])
            s_i += 1

        visited_char.add(char)
        longuest_str = max(longuest_str, s_j - s_i + 1)
        s_j += 1

    return longuest_str


if __name__ == "__main__":
    print(longuest_substr("abcabcbb"))
    print(longuest_substr("bbbbb"))
    print(longuest_substr("pwwkew"))
