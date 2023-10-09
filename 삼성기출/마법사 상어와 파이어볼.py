def move(r, c, m, s, d, index):
    x, y = direction[d]

    x *= s
    y *= s

    x = x % N
    y = y % N

    if r + x < 0:
        x = N + x
    if c + y < 0:
        y = N + y

    r = (r + x) % N
    c = (c + y) % N

    ball_map[r][c].append(index)
    return [r, c, m, s, d]


def change_status(r, c, index_list):
    all_m = 0
    all_s = 0
    all_d = 0
    for i in range(len(index_list)):
        temp = ball_list[index_list[i]]
        all_m += temp[2]
        all_s += temp[3]
        all_d += temp[4] % 2

    value_m = all_m // 5
    value_s = all_s // len(index_list)

    if value_m == 0:
        return

    first_route = [0, 2, 4, 6]
    second_route = [1, 3, 5, 7]
    if all_d == 0 or all_d == len(index_list):
        for i in range(4):
            new_ball_list.append([r, c, value_m, value_s, first_route[i]])
    else:
        for i in range(4):
            new_ball_list.append([r, c, value_m, value_s, second_route[i]])


N, ball_count, move_times = map(int, input().split())

ball_list = [list(map(int, input().split())) for _ in range(ball_count)]
for i in range(len(ball_list)):
    if 0 < ball_list[i][0] <= N:
        ball_list[i][0] = ball_list[i][0] - 1
    if 0 < ball_list[i][1] <= N:
        ball_list[i][1] = ball_list[i][1] - 1


# 방향 정하는 딕셔너리
direction = {}
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(8):
    direction[i] = (dx[i], dy[i])

# 볼 이동하기
for _ in range(move_times):
    # 볼이 위치한 곳 저장하는 map
    ball_map = [[[] for _ in range(N)] for _ in range(N)]

    one_list = []
    many_list = []

    for i in range(len(ball_list)):
        ball_list[i] = move(
            ball_list[i][0],
            ball_list[i][1],
            ball_list[i][2],
            ball_list[i][3],
            ball_list[i][4],
            i,
        )
    new_ball_list = []
    for i in range(N):
        for j in range(N):
            new_location_ball = ball_map[i][j]
            if len(ball_map[i][j]) == 1:
                new_ball_list.append(ball_list[new_location_ball[0]])
            elif len(ball_map[i][j]) > 1:
                change_status(i, j, new_location_ball)

    ball_list = new_ball_list[:]
    if len(new_ball_list) == 0:
        break

answer = 0
for r, c, m, s, d in new_ball_list:
    answer += m

print(answer)
