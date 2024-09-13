def two_sums(nums, target):
    for index, item in enumerate(nums):
        if target - item in nums and nums.index(target - item) is not index:
            return [index, nums.index(target - item)]
    return -1


if __name__ == "__main__":
    print(two_sums([2, 7, 11, 15], 9))
    print(two_sums([3, 2, 4], 6))
    print(two_sums([3, 3], 6))
