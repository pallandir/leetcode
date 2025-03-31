def flood_fill(grid,row,col,new_color):
    previous_color = grid[row][col]
    if previous_color == new_color:
        return

    # process neighbors
    rows,cols = len(grid), len(grid[0])
    queue = [(row,col)]
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    while queue:
        cur_row,cur_col = queue.pop(0)
        grid[cur_row][cur_col] = new_color
        for d_row,d_col in directions:
            new_row,new_col = cur_row + d_row, cur_col+ d_col
            if 0 <= new_row < rows and 0 <= new_col <cols and grid[new_row][new_col] == previous_color:
                queue.append((new_row,new_col))


if __name__ == "__main__":
    grid = [[1,1,0,0],[1,0,0,1],[1,1,1,1]]
    print(grid)
    flood_fill(grid,0,0,5)
    print(grid)
