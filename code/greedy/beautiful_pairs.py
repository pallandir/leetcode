from typing import Counter


def beatiful_pairs(first_list, second_list):
    first_counter = Counter(first_list)
    second_counter = Counter(second_list)
    matches = 0
    for number in first_list:
        matches += min(first_counter.get(number, 0), second_counter.get(number, 0))

    return matches + 1 if matches < len(first_list) else matches - 1


if __name__ == "__main__":
    print(beatiful_pairs([1, 2, 3, 4], [1, 2, 3, 3]))
    print(beatiful_pairs([3, 5, 7, 11, 5, 8], [5, 7, 11, 10, 5, 8]))
