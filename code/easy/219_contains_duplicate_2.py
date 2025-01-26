def contains_duplicates(nums: list, k: str):
    hash_map = {}

    for index, value in enumerate(nums):
        print(hash_map, value, index)
        if value in hash_map and index - hash_map[value] <= k:
            return True
        hash_map[value] = index
    return False


if __name__ == "__main__":
    print(contains_duplicates([1, 2, 3, 1], 3))
