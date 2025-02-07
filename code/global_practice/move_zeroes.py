def move_zeroes(nums):
    i, j = 0, 0

    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1


if __name__ == "__main__":
    my_list = [1, 0, 2, 0, 0, 7]
    move_zeroes(my_list)
    print(my_list)
