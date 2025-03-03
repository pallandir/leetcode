def min_cost_step(cost: list[int]):
    prev_cost, curr_cost = 0, 0

    for index in range(2, len(cost) + 1):
        temp_prev_cost = curr_cost
        curr_cost = min(prev_cost + cost[index - 2], curr_cost + cost[index - 1])
        prev_cost = temp_prev_cost
    return curr_cost


if __name__ == "__main__":
    print(min_cost_step([10, 15, 20]))
