def max_subarray(nums):
    hashset = set(nums)
    count = 0
    for num in hashset:
        if num - 1 not in hashset: #start to count only if the smallest value is found
            current_len = 1
            while (num + current_len) in hashset:
                current_len += 1
        count = max(count, current_len)
    return count


if __name__ == "__main__":
    print(max_subarray([1, 2, 3, 4, 10, 20]))
