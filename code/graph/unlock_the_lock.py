def unlock_the_lock(end, deadlock):
    base_combination = "0000"
    if base_combination in deadlock:
        return -1

    visited = set(base_combination)
    queue = [(base_combination, 0)]

    while queue:
        current_combination, moves = queue.pop(0)

        if current_combination == end:
            return moves

        for index in range(4):
            combination_digits = int(current_combination[index])
            for move in [-1, 1]:
                new_combination_digit = (combination_digits + move) % 10
                new_combination = (
                    current_combination[:index]
                    + str(new_combination_digit)
                    + current_combination[index + 1 :]
                )

                if new_combination not in deadlock and new_combination not in visited:
                    visited.add(current_combination)
                    queue.append((new_combination, moves + 1))
    return -1


if __name__ == "__main__":
    print(unlock_the_lock("0202", ["0201", "0101", "0102", "1212", "2002"]))
