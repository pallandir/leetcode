def reverseVowels(s: str):
    i = 0
    j = len(s) - 1
    s = list(s)
    vowels = ["a", "e", "i", "o", "u"]

    while i < j:
        if s[i].lower() not in vowels:
            i += 1
            continue
        if s[j].lower() not in vowels:
            j -= 1
            continue

        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)


if __name__ == "__main__":
    s = "IceCreAm"

    print(reverseVowels(s))
