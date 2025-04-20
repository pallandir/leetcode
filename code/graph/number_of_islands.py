def number_of_island(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def get_neighbour(row, col):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbour = []
        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbour.append((new_r, new_c))
        return neighbour

    def bfs(row, col):
        queue = [(row, col)]

        while queue:
            cur_row, cur_col = queue.pop(0)
            for neighbour in get_neighbour(cur_row, cur_col):
                cur_row, cur_col = neighbour
                if grid[cur_row][cur_col] == "0":
                    continue
                queue.append((cur_row, cur_col))
                grid[cur_row][cur_col] = "0"

    island_number = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "0":
                continue
            bfs(row, col)
            island_number += 1
    return island_number


if __name__ == "__main__":
    print(
        number_of_island(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
