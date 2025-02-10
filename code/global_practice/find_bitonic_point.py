def find_bitonic_point(array):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid - 1] < array[mid] and array[mid] > array[mid + 1]:
            return mid
        elif array[mid] < array[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(find_bitonic_point([6, 7, 8, 11, 9, 5, 2, 1]))
