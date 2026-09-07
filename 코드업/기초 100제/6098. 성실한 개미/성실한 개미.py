board = [list(map(int, input().split())) for _ in range(10)]
row = column = 1
while True:
    if board[row][column] == 2:
        board[row][column] = 9
        break
    board[row][column] = 9
    if board[row][column + 1] == 1:
        if board[row + 1][column] == 1:
            break
        row += 1
    else:
        column += 1
for row in board:
    print(*row)
