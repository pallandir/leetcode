from collections import Counter


def majority_element(nums):
    for key, _ in Counter(nums).most_common(1):
        return key


if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element([3, 2, 3]))
