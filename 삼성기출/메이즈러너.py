# N은 격자, M은 참가자의 수, K는 초
import copy

N, M, K = map(int, input().split())

# 0 빈칸
# -1 ~ -9 벽으로 하고
# 1부터는 사람의 수
# 출구는 -10
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        temp[j] = -temp[j]
    board.append(temp)

for i in range(M):
    x, y = map(int, input().split())
    board[x - 1][y - 1] += 1

exit_x, exit_y = map(int, input().split())
board[exit_x - 1][exit_y - 1] = -10
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_exit():
    for i in range(N):
        for j in range(N):
            if board[i][j] == -10:
                return (i, j)
def move():
    global move_count
    # 새로운 보드를 만들고
    new_board = [[0] * N for _ in range(N)]
    # 출구 좌표 찾고
    exit_x, exit_y = find_exit()

    # 모든 행열을 돌면서, 사람이 있으면, 가까운 곳으로 옮기기
    for rx in range(N):
        for ry in range(N):
            # 0보다 작거나 0 이면 빈칸이거나 벽이기 때문에 사람이 아님
            if board[rx][ry] < 0:
                new_board[rx][ry] = board[rx][ry]
                continue
            if board[rx][ry] == 0:
                continue
            # 사람이라면 현재 위치에서 출구까지 거리를 구한다.
            cur_dist = abs(exit_x - rx) + abs(exit_y - ry)
            min_dist = cur_dist
            # 상하좌우 우선순위로 돌면서 현재 위치보다 가까운 거리를 찾는다.
            for i in range(4):
                tx = rx + dx[i]
                ty = ry + dy[i]
                # 만약 격자 밖으로 나간다면 패스
                if tx < 0 or ty < 0 or tx >= N or ty >= N:
                    continue
                # 만약 -1 부터 -9 까지면 벽이기 때문에 패스
                if -9 <= board[tx][ty] <= -1:
                    continue
                # 만약에 현재위치-출구 거리보다 새로운 곳의 거리가 더 짧다면
                if cur_dist > abs(exit_x - tx) + abs(exit_y - ty):
                    min_dist = abs(exit_x - tx) + abs(exit_y - ty)
                    min_x = tx
                    min_y = ty

            if min_dist == cur_dist:
                new_board[rx][ry] += board[rx][ry]
                continue
            # 이동거리 더해주고
            move_count += board[rx][ry]

            # 만약에 이동한 곳이 출구면 굳이 격자에 옮길 이유는 없음
            if (min_x, min_y) == (exit_x, exit_y):
                continue
            # 움직인거라면, 뉴 보드에는 +=
            new_board[min_x][min_y] += board[rx][ry]

    for i in range(N):
        for j in range(N):
            board[i][j] = new_board[i][j]



def rotate(x, y, l):
    temp = [[0] * N for _ in range(N)]
    # 행 x 시작점
    # 열 y 시작점
    for r in range(x, x + l):
        for c in range(y, y + l):
            temp[c][r-l-1] = board[r][c]

    for i in range(x, x + l):
        for j in range(y, y + l):
            board[i][j] = temp[i][j]

    for i in range(x, x + l):
        for j in range(y, y + l):
            if board[i][j] != -10 :
                board[i][j] = board[i][j] -1
            else :
                board[i][j] = board[i][j]

def find_sq():
    # 1. 정사각격의 사이즈 먼저 구하기
    min_dist = 10000
    best_x = 0
    best_y = 0
    exit_x, exit_y = find_exit()

    for i in range(N):
        for j in range(N):
            if board[i][j] <= 0: continue
            dist = max(abs(exit_x - i), abs(exit_y - j)) + 1
            min_dist = min(min_dist, dist)

    # 2. 정사각형의 사이즈 만큼의 좌표의 시작이 어디서 부터인지 구하기
    for i in range(N - min_dist):
        for j in range(N - min_dist):
            exit_check = False
            person_check = False
            for x in range(i, i + min_dist):
                for y in range(j, j + min_dist):
                    if exit_x == x and exit_y == y:
                        exit_check = True
                    if board[x][y] > 0:
                        person_check = True

            if (exit_check and person_check):
                best_x = i
                best_y = j
                break
        if best_x != 0:
            break

    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                count += 1
    if count == 0:
        return

    rotate(best_x, best_y, min_dist)
    return

move_count = 0
while K:
    # 1. 사람들이 출구와 가장 가까운 방향으로 옮기기
    move()
    # 2. 출구와 사람의 거리가 제일 작은 거리큼의 정사각형 찾기
    find_sq()
    # 3. 그 정사각형에 있는 걸 90도 회전하고, 내구도 1씩 깍기
    K -= 1

print(move_count)
x, y = find_exit()
print(x + 1, y + 1)
