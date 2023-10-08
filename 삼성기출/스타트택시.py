import copy
from collections import deque


# 입력 받기
N, customer_num, gas = map(int, input().split())
town_map = [list(map(int, input().split())) for i in range(N)]
taxi_x, taxi_y = map(int, (input().split()))
customer_list = [list(map(int, input().split())) for i in range(customer_num)]

taxi_x -= 1
taxi_y -= 1


for i in range(len(customer_list)):
    for j in range(4):
        if customer_list[i][j] != 0:
            customer_list[i][j] = customer_list[i][j] - 1


def short_distance(start_x, start_y):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while len(q) != 0:
        real_x, real_y = q.popleft()

        for i in range(4):
            x = real_x + dx[i]
            y = real_y + dy[i]

            if x < 0 or y < 0 or x >= N or y >= N:
                continue
            if town_map[x][y] == 1 or visited[x][y] != 0:
                continue

            visited[x][y] = visited[real_x][real_y] + 1
            q.append((x, y))

    return visited


while len(customer_list) > 0:
    custom_distance_list = []
    visited = short_distance(taxi_x, taxi_y)
    for i in range(len(customer_list)):
        custom_distance_list.append(
            visited[customer_list[i][0]][customer_list[i][1]] - 1
        )
    if -1 in custom_distance_list:
        gas = -1
        break

    # 어떤 손님의 위치가 택시랑 더 가까운지.
    min_index = 0
    for j in range(1, len(custom_distance_list)):
        if custom_distance_list[j] < custom_distance_list[min_index]:
            min_index = j
        elif custom_distance_list[j] == custom_distance_list[min_index]:
            if customer_list[j][0] < customer_list[min_index][0]:
                min_index = j
            elif customer_list[j][0] == customer_list[min_index][0]:
                if customer_list[j][1] < customer_list[min_index][1]:
                    min_index = j

    pick_up_gas = custom_distance_list[min_index]
    gas -= pick_up_gas

    if gas < 0:
        gas = -1
        break

    temp = short_distance(customer_list[min_index][0], customer_list[min_index][1])
    customer_gas = temp[customer_list[min_index][2]][customer_list[min_index][3]] - 1
    gas -= customer_gas

    if gas < 0:
        gas = -1
        break

    taxi_x = customer_list[min_index][2]
    taxi_y = customer_list[min_index][3]
    del customer_list[min_index]
    gas += customer_gas * 2

print(gas)
