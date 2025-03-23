def get_neighbors(grid, row, col):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbors = []
    for dr, dc in directions:
        new_r, new_c = row + dr, col + dc
        if 0 <= new_r < rows and 0 <= new_c < cols:
            neighbors.append(grid[new_r][new_c])
    return neighbors


if __name__ == "__main__":
    grid = [
        [0, 1, 3, 4, 1],
        [3, 8, 8, 3, 3],
        [6, 7, 8, 8, 3],
        [12, 2, 8, 9, 1],
        [12, 3, 1, 3, 2],
    ]
    print(get_neighbors(grid, 2, 2))
    print(get_neighbors(grid, 0, 0))
