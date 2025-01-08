def check_ransom_note(ransomNote, magazine):
    ransom_freq = {char: ransomNote.count(char) for char in set(ransomNote)}
    magazine_frq = {char: magazine.count(char) for char in set(magazine)}

    for char, freq in ransom_freq.items():
        if magazine_frq.get(char, 0) < freq:
            return False

    return True


if __name__ == "__main__":
    print(check_ransom_note("a", "b"))
    print(check_ransom_note("aa", "ab"))
    print(check_ransom_note("aa", "aab"))
    print(check_ransom_note("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))
    print(check_ransom_note("aab", "baa"))
