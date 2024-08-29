from collections import defaultdict


def rotate_array(nums):
    if len(nums) < 3:
        return len(nums)
    freq = defaultdict(int)
    nums[:] = [
        num
        for num in nums
        if freq[num] < 2 and not freq.__setitem__(num, freq[num] + 1)
    ]
    return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    rotate_array(nums)
    print(nums)
