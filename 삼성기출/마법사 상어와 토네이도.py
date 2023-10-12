import copy
from collections import deque


def move(start, d, y_count):
    check = 0
    a_x = 0
    a_y = 0
    rest = 0

    y_x, y_y = start[0] + dx[d], start[1] + dy[d]

    y_value = town[y_x][y_y]

    for i in range(8):
        rx = y_x + dx[i]
        ry = y_y + dy[i]

        if tornado[i] == 'a':
            if rx < 0 or ry < 0 or rx >= N or ry >= N:
                a_x = -1
                a_y = -1
            else:
                a_x = copy.deepcopy(rx)
                a_y = copy.deepcopy(ry)

            rx += dx[d]
            ry += dy[d]

            temp2 = (5 / 100) * y_value
            if rx < 0 or ry < 0 or rx >= N or ry >= N:
                rest += int(temp2)
                continue
            town[rx][ry] += int(temp2)
            check += int(temp2)

        else:
            temp3 = (tornado[i] / 100) * y_value
            if rx < 0 or ry < 0 or rx >= N or ry >= N:
                rest += int(temp3)
                continue
            else:
                town[rx][ry] += int(temp3)
                check += int(temp3)
                if tornado[i] == 7:
                    rx = y_x + (dx[y_check[y_count]] * 2)
                    ry = y_y + (dy[y_check[y_count]] * 2)
                    temp2 = (2 / 100) * y_value
                    if rx < 0 or ry < 0 or rx >= N or ry >= N:
                        rest += int(temp2)
                        continue
                    town[rx][ry] += int(temp2)
                    check += int(temp2)
                    y_count += 1
                    if y_count == 4:
                        y_count = 0

    town[y_x][y_y] = 0

    if a_x >= 0 and a_y >= 0:
        town[a_x][a_y] += y_value - check
    else:
        rest += int(y_value - check)
    return (y_x, y_y), y_count, rest

N = int(input().strip())
town = []

y_check = [2, 6, 0, 4]
y_count = 0

for i in range(N):
    temp = list(map(int, input().split()))
    # all += sum(temp)
    town.append(temp)

tornado = deque(['a', 10, 7, 1, 0, 1, 7, 10])

four_d = [0, 6, 4, 2]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
loop = 1
start = (N // 2, N // 2)
d_count = 0
rest_original = 0

while loop < N:
    for i in range(2):
        for j in range(loop):
            start, y_count, rest = move(start, four_d[d_count], y_count)
            rest_original += rest
        d_count += 1
        for _ in range(2):
            tmp = tornado.popleft()
            tornado.append(tmp)
        if d_count == 4:
            d_count = 0
    if loop == N-1 and d_count == 0 :
        start, y_count, rest = move(start, four_d[d_count], y_count)
        rest_original += rest
        break

    loop += 1

print(rest_original)
