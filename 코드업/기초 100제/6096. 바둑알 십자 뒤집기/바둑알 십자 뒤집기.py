board = [list(map(int, input().split())) for _ in range(19)]
count = int(input())
for _ in range(count):
    row, column = map(int, input().split())
    for index in range(19):
        board[row - 1][index] ^= 1
        board[index][column - 1] ^= 1
for row in board:
    print(*row)
