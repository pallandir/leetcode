def remove_duplicates(duplicates_lst):
    i, j = 0, 0

    while j < len(duplicates_lst):
        if duplicates_lst[i] != duplicates_lst[j]:
            i += 1
            duplicates_lst[i] = duplicates_lst[j]
        j += 1
    return i + 1


def find_middle(values_lst):
    i, j = 0, len(values_lst) - 1

    while i <= j:
        middle = values_lst[j]
        i += 1
        j -= 1
    return middle


if __name__ == "__main__":
    duplicates = [0, 0, 1, 1, 1, 2, 2]
    # values_lst = [0, 1, 2, 3, 4]
    values_lst = [0, 1, 2, 3, 4, 5]
    print(find_middle(values_lst))
