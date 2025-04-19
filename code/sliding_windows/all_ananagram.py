from typing import Counter


def all_anagrams(string, word):
    if len(string) < len(word):
        return []

    result = []
    word_len = len(word)
    frequencies_ref = Counter(word)

    for index in range(len(string) - word_len + 1):
        current_window = string[index : index + word_len]
        if Counter(current_window) == frequencies_ref:
            result.append(index)

    return result


if __name__ == "__main__":
    print(all_anagrams("cbaebabacd", "abc"))
