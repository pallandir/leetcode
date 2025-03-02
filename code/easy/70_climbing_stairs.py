def climbing_stairs(n: int):
    prev_step, curr_step = 0, 1

    for _ in range(n):
        prev_step, curr_step = curr_step, curr_step + prev_step

    return curr_step


if __name__ == "__main__":
    print(climbing_stairs(2))
    print(climbing_stairs(3))
