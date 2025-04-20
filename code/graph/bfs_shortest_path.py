def shortest_path(grid, start, end):
    def get_neighbor(grid, row, col):
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbor = []
        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbor.append((new_r, new_c))
        return neighbor

    path = []

    queue = [(start, [start])]
    visited = set()

    while queue:
        (cur_row, cur_col), path = queue.pop(0)
        if (cur_row, cur_col) == end:
            return path
        if (cur_row, cur_col) in visited:
            continue
        visited.add((cur_row, cur_col))
        for neighbor in get_neighbor(grid, cur_row, cur_col):
            cur_row, cur_col = neighbor
            if grid[cur_row][cur_col] == "1":
                continue
            queue.append((neighbor, path + [neighbor]))

    return None


if __name__ == "__main__":
    print(
        shortest_path(
            [
                ["0", "0", "1", "0"],
                ["1", "0", "1", "0"],
                ["0", "0", "0", "0"],
                ["0", "1", "1", "0"],
            ],
            (0, 0),
            (3, 3),
        )
    )
