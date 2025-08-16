def pair_sum(num_list, target):
    left, right = 0, len(num_list) - 1
    all_sums = []
    while left <= right:
        print(left, right)
        sum = num_list[left] + num_list[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            all_sums.append([left, right])
            left += 1
            right -= 1
    return all_sums


if __name__ == "__main__":
    print(pair_sum([-5, -3, 1, 3, 4, 6], 7))
