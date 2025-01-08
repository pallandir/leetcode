# complexity : concat : O(m+n) + sort O(log(m+n))
def merge_array(array1, array2, m, n):
    array1[:] = sorted(array1[:m] + array2[:n])


def merge_array_2(array1, array2, m, n):
    array1[m:] = array2[:n]


def merge_array_3(array1, array2, m, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and array1[i] > array2[j]:
            array1[k] = array1[i]
            i -= 1
        else:
            array1[k] = array2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge_array_3(nums1, nums2, m, n)

    print(nums1)
