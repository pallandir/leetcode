def greedy_florist(flowers, friends):
    flowers.sort(reverse=True)
    total_cost = 0
    for index in range(len(flowers)):
        total_cost += index // friends + 1 * flowers[index]

    return total_cost


if __name__ == "__main__":
    print(greedy_florist([1, 2, 3, 4], 3))
    print(greedy_florist([2, 5, 6], 3))
    print(greedy_florist([2, 5, 6], 2))
    print(greedy_florist([1, 3, 5, 7, 9], 2))
