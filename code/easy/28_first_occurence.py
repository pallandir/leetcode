def first_occurence(haystack, needle):
    if not needle or len(needle) > len(haystack):
        return 0
    i = 0

    while i <= len(haystack) - len(needle):
        if haystack[i : i + len(needle)] == needle:
            return i
        i += 1

    return -1


if __name__ == "__main__":
    print(first_occurence("sadbutsad", "sad"))
    print(first_occurence("leetcode", "leeto"))
    print(first_occurence("hello", "ll"))
