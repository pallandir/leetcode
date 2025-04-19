def greedy_florist(flowers, friends):
    base_sum = sum(flowers[-friends:])
    for index in range(len(flowers) - friends):
        base_sum += ((index + 1) + 1) * flowers[index]

    return base_sum


if __name__ == "__main__":
    print(greedy_florist([1, 2, 3, 4], 3))
    print(greedy_florist([2, 5, 6], 3))
    print(greedy_florist([2, 5, 6], 2))
