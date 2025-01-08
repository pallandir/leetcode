def remove_duplicates(nums):
    nums[:] = {key: 1 for key in nums}.keys()
    return len(nums)


def remove_duplicates2(nums):
    print(dict.fromkeys(nums))
    nums[:] = dict.fromkeys(nums).keys()


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    nums = [-1, 0, 0, 0, 0, 3, 3]
    remove_duplicates2(nums)
    print(nums)
