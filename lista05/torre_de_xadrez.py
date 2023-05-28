board_size = 8
chessboard = [[int(n) for n in input().split()] for _ in range(board_size)]
x, y = [int(n) for n in input().split()]
enemies = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

for dir_x, dir_y in directions:
    i, j = x + dir_x, y + dir_y

    while 0 <= i < board_size and 0 <= j < board_size:
        if chessboard[i][j] == 1:
            break
        elif chessboard[i][j] == 2:
            enemies += 1
            break
        i += dir_x
        j += dir_y

print(enemies)
