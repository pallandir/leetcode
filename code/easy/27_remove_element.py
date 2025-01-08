def remove_element(nums, val):
    nums[:] = [num for num in nums if num != val]
    return len(nums)


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    remove_element(nums, 3)
    print(nums)
