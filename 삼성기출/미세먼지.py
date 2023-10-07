import copy


def upside_wind(up):
    upside_list = []

    for i in range(1, C):
        upside_list.append([up, i])
    for i in range(up - 1, -1, -1):
        upside_list.append([i, C - 1])
    for i in range(C - 2, -1, -1):
        upside_list.append([0, i])
    for i in range(1, up):
        upside_list.append([i, 0])
    return upside_list


def downside_wind(down):
    downside_list = []

    for i in range(1, C):
        downside_list.append([down, i])
    for i in range(down + 1, R - 1):
        downside_list.append([i, C - 1])
    for i in range(C - 1, -1, -1):
        downside_list.append([R - 1, i])
    for i in range(R - 2, down, -1):
        downside_list.append([i, 0])
    return downside_list


def moving_wind(change_area, wind):
    temp1 = copy.deepcopy(change_area[wind[0][0]][wind[0][1]])
    change_area[wind[0][0]][wind[0][1]] = 0
    for i in range(0, len(wind) - 1):
        temp2 = copy.deepcopy(change_area[wind[i + 1][0]][wind[i + 1][1]])
        change_area[wind[i + 1][0]][wind[i + 1][1]] = temp1
        temp1 = temp2

    return change_area


R, C, T = map(int, input().split())

air_area = [list(map(int, input().split())) for i in range(R)]
check = "True"
machine = []

for i in range(R):
    if air_area[i][0] == -1:
        air_area[i][0] = check
        check = "False"
        machine.append(i)

up_list = upside_wind(machine[0])
down_list = downside_wind(machine[1])

for i in range(T):
    change_area = [[0 for _ in range(C)] for _ in range(R)]

    air_area[machine[0]][0] = "True"
    air_area[machine[1]][0] = "False"
    for r in range(R):
        for c in range(C):
            if air_area[r][c] == "True" or air_area[r][c] == "False":
                continue
            if air_area[r][c] == 0:
                continue

            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            count = 0

            for i in range(4):
                x = r + dx[i]
                y = c + dy[i]

                if x < 0 or y < 0 or x >= R or y >= C:
                    continue
                if air_area[x][y] == "True":
                    continue
                if air_area[x][y] == "False":
                    continue
                temp = air_area[r][c] // 5
                change_area[x][y] += temp
                count += 1

            change_area[r][c] = (
                change_area[r][c] + air_area[r][c] - ((air_area[r][c] // 5) * count)
            )

    change_area = copy.deepcopy(moving_wind(change_area, up_list))
    change_area = copy.deepcopy(moving_wind(change_area, down_list))
    air_area = copy.deepcopy(change_area)

all = 0
for i in range(R):
    m = sum(air_area[i])
    all += m

print(all)
