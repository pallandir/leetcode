def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0

    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


def isSubsequence2(s: str, t: str):
    i, j = 0, 0
    while j < len(t) and i < len(s):
        if t[j] == s[i]:
            i += 1
        j += 1
    return i == len(s)


if __name__ == "__main__":
    string = "ahbgdc"
    substr = "abc"

    print(isSubsequence(substr, string))
