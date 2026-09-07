count = int(input())
board = [[0] * 19 for _ in range(19)]
for _ in range(count):
    row, column = map(int, input().split())
    board[row - 1][column - 1] = 1
for row in board:
    print(*row)
