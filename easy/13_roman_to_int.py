def roman_to_int(s):
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    number = 0
    s_inverted = s[::-1]

    for index, char in enumerate(s_inverted):
        if map[char] < map[s_inverted[index - 1]] and index > 0:
            number -= map[char]
        else:
            number += map[char]

    return number


if __name__ == "__main__":
    numbers: list = ["III", "LVIII", "MCMXCIV"]

    for s in numbers:
        print(roman_to_int(s))
