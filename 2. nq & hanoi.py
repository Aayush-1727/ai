1. N-queen

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def check_queen(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

        j = row - i
        if col - j >= 0 and board[i][col-j] == 'Q':
            return False

        if col + j < n and board[i][col+j] == 'Q':
            return False

    return True


def solve_queen(board, row, n):
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if check_queen(board, row, col, n):
            board[row][col] = 'Q'

            if solve_queen(board, row + 1, n):
                return True

            board[row][col] = '.'

    return False


def queens():
    n = int(input("Enter value of N: "))
    board = []

    for i in range(n):
        board.append(['.'] * n)

    if not solve_queen(board, 0, n):
        print("No solution found")


queens()

2. Hanoi

def hanoi(n, source, helper, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    hanoi(n - 1, source, destination, helper)

    print("Move disk", n, "from", source, "to", destination)

    hanoi(n - 1, helper, source, destination)


n = int(input("Enter the no. of disk: "))

hanoi(n, 'A', 'B', 'C')