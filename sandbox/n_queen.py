def solve_n_queens(queens):
    result = []

    def generate_solutions(row, board):
        if row == queens:
            result.append(board[:])  # shallow copy
            return

        for col in range(queens):
            if valid_position(row, col, board):
                board[row] = col
                generate_solutions(row + 1, board)
                board[row] = -1

    board = [-1] * queens
    generate_solutions(0, board)
    return result


def valid_position(row, col, board):
    for index in range(row):
        if (
            board[index] == col  # if a queen is already placed in the same column
            or board[index] - index
            == col - row  # If there is a queen on the major diagonal (top left to bottom right)
            or board[index] + index
            == row + col  # If there is a queen on the minor diagonal (top right to bottom left)
        ):
            return False

    return True


def parse_board(boards):
    for solution in boards:
        print(f"Solution board : {solution}")
        for _, col in enumerate(solution):
            print(" . " * col + " q " + " . " * (len(solution) - col - 1))
        print("\n")


if __name__ == "__main__":
    queens = 4
    boards_solutions = solve_n_queens(queens)
    parse_board(boards_solutions)
