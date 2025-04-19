def marcs_cakewalk(calories: list[int]):
    calories.sort(reverse=True)
    walk_distance = 0

    for index, calorie in enumerate(calories):
        walk_distance += 2**index * calorie

    return walk_distance


if __name__ == "__main__":
    print(marcs_cakewalk([5, 10, 7]))
    print(marcs_cakewalk([1, 3, 2]))
