def reverse_words(s: str):
    return " ".join(s.strip().split()[::-1])


if __name__ == "__main__":
    print(reverse_words("the sky is blue"))
    print(reverse_words("  hello world  "))
    print(reverse_words("a good   example"))
