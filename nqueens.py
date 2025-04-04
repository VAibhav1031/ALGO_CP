def nqueens(board, row: int):
    if row == len(board):
        display(board)
        print()
        print(display1(board))
        print()
        return 1

    count = 0  # this will return the amount of the correct formations we have formed till now
    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = True  # Place the queen
            count += nqueens(board, row + 1)
            board[row][col] = False  # Backtrack

    return count

def isSafe(board, row: int, col: int):
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    min_left = min(row, col)
    for i in range(1, min_left + 1):
        if board[row - i][col - i]:
            return False

    # Check upper right diagonal
    min_right = min(row, len(board) - col - 1)
    for i in range(1, min_right + 1):
        if board[row - i][col + i]:
            return False

    return True

def display(board):
    for row in board:
        for element in row:
            if element:
                print('Q', end=" ")
            else:
                print("X", end=" ")
        print()


def display1(board):
    result = []
    for row in board:
        row_ = []
        for element in row:
            if element:
                row_.append('Q')
            else:
                row_.append(".")
        result.append(row_)
    return result

# Initialize the board

if __name__ == "__main__":
    n = int(input())
    board = [[False] * n for _ in range(n)]
    print(nqueens(board, 0))