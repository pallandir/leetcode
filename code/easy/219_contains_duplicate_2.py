def containsDuplicates2(nums: list, k: str):
    hash_map = {}

    for index, value in enumerate(nums):
        print(hash_map, value, index)
        if value in hash_map and index - hash_map[value] <= k:
            return True
        hash_map[value] = index
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3

    print(containsDuplicates2(nums, k))
