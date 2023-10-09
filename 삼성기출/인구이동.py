from collections import deque

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for i in range(N)]


def bfs(i, j, visited):
    change = [(i, j)]
    visited[i][j] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((i, j))

    while q:
        rx, ry = q.popleft()
        for i in range(4):
            x = rx + dx[i]
            y = ry + dy[i]

            if x < 0 or y < 0 or x >= N or y >= N:
                continue
            if visited[x][y] == 1:
                continue
            if L <= abs(country[rx][ry] - country[x][y]) <= R:
                visited[x][y] = 1
                q.append((x, y))
                change.append((x, y))

    return change if len(change) > 1 else []


check = True
answer = 0
while check:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    check = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                change = bfs(i, j, visited)

                if len(change) > 0:
                    check = True
                    all = 0
                    for x, y in change:
                        all += country[x][y]
                    value = all // len(change)
                    for x, y in change:
                        country[x][y] = value

    if check == False:
        break
    answer += 1

print(answer)
