def sub_array_sum(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    print(sub_array_sum([1, 2, 3, 7, 4, 1], 3))
