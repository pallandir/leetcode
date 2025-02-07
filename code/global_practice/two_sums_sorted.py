def two_sums_sorted(nums, target):
    i, j = 0, len(nums) - 1

    while i < j:
        sum = nums[i] + nums[j]
        if sum == target:
            return (i, j)

        if nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1

    return -1


if __name__ == "__main__":
    print(two_sums_sorted([2, 3, 4, 5, 8, 11, 18], 8))
