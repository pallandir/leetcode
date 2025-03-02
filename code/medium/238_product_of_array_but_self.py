def nums_array_product(nums: list):
    nums_size = len(nums)
    ans = [0] * nums_size
    prefix_acc = 1
    postfix_acc = 1

    # accumulate from left to nums[i]
    for index, number in enumerate(nums):
        ans[index] = prefix_acc
        prefix_acc *= number

    # accumulate fro right nums[i]
    for index, number in enumerate(nums[::-1]):
        ans[nums_size - 1 - index] *= postfix_acc
        postfix_acc *= number

    return ans


if __name__ == "__main__":
    print(nums_array_product([1, 2, 3, 4]))
