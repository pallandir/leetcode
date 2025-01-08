def rotate_array(nums, k):
    nums[:] = [nums[(i - k) % len(nums)] for i in range(len(nums))]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(nums, 3)
    print(nums)
