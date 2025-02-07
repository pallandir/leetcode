def first_element_not_smaller(array, target):
    left, right = 0, len(array) - 1
    first_occ = -1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] >= target:
            first_occ = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_occ


if __name__ == "__main__":
    # return the index of the first element not smaller than the target, here 3
    print(first_element_not_smaller([1, 1, 3, 4, 4, 5], 2))
