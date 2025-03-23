def first_occurence(array, target):
    left, right = 0, len(array) - 1
    first_occ = -1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            first_occ = mid
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first_occ


if __name__ == "__main__":
    print(first_occurence([1, 1, 2, 2, 2, 2, 3, 4, 4, 5], 2))
