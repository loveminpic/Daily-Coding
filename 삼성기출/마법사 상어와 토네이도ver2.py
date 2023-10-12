import copy

N = int(input().strip())
board = [list(map(int, input().split())) for i in range(N)]

start = (N // 2, N // 2)
check_d = 0
loop = 1
tornado = [1, 2, 5, 7, 10]

left_down_right_up = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = [
    [[(-1, 1), (1, 1)], [(-2, 0), (2, 0)], [(0, -2)], [(-1, 0), (1, 0)], [(-1, -1), (1, -1)]], # 0
    [[(-1, -1), (-1, 1)], [(0, -2), (0, 2)], [(2, 0)], [(0, -1), (0, 1)], [(1, -1), (1, 1)]],  # 1
    [[(-1, -1), (1, -1)], [(-2, 0), (2, 0)], [(0, 2)], [(-1, 0), (1, 0)], [(-1, 1), (1, 1)]],  # 2
    [[(1, -1), (1, 1)], [(0, -2), (0, 2)], [(-2, 0)], [(0, -1), (0, 1)], [(-1, -1), (-1, 1)]], # 3
]
result = 0


def move(start, check_d):
    global result
    d = left_down_right_up[check_d]
    y_x, y_y = start[0] + d[0], start[1] + d[1]
    direct = direction[check_d]
    temp = board[y_x][y_y]
    sand_moved = 0

    for i in range(len(tornado)):
        for x,y in direct[i] :
            rx = y_x + x
            ry = y_y + y

            value = temp * tornado[i] // 100
            sand_moved += value
            if 0 <= rx < N and 0 <= ry < N:
                board[rx][ry] += value
            else:
                result += value

    ax, ay = y_x + d[0], y_y + d[1]
    remaining_sand = temp - sand_moved
    if 0 <= ax < N and 0 <= ay < N:
        board[ax][ay] += remaining_sand
    else:
        result += remaining_sand

    board[y_x][y_y] = 0
    return (y_x, y_y)


while loop < N:
    for i in range(2):
        for j in range(loop):
            start = move(start, check_d)

        check_d = (check_d + 1) % 4
    if loop == N - 1:
        for j in range(loop):
            if start == (0,0):
                break
            start = move(start, 0)
    loop += 1
print(result)
