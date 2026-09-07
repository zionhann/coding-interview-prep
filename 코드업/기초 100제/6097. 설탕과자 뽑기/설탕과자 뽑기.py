height, width = map(int, input().split())
count = int(input())
board = [[0] * width for _ in range(height)]
for _ in range(count):
    length, direction, row, column = map(int, input().split())
    for offset in range(length):
        if direction == 0:
            board[row - 1][column - 1 + offset] = 1
        else:
            board[row - 1 + offset][column - 1] = 1
for row in board:
    print(*row)
