def moveZeroes(nums: list[int]):
    i,j = 0,0

    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(nums)
    moveZeroes(nums)
    print(nums)
