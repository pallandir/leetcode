def valid_palindrome(nums, target):
    for index, item in enumerate(nums):
        if target - item in nums and nums.index(target - item) is not index:
            return [index, nums.index(target - item)]
    return -1


if __name__ == "__main__":
    print(valid_palindrome([2, 7, 11, 15], 9))
    print(valid_palindrome([3, 2, 4], 6))
    print(valid_palindrome([3, 3], 6))
