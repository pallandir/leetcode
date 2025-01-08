def maxValues(nums: list, k: str):
    i, size = 0, len(nums)
    max_values = []
    while i <= size - k:
        print(i, nums[i : i + k])
        max_values.append(max(nums[i : i + k]))
        i += 1
    return max_values


if __name__ == "__main__":
    nums = [1, 3, 2, 5, 8, 7]
    k = 3

    print(maxValues(nums, k))
