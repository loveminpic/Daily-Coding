from collections import deque


def rotate(r, c, l):
    global board
    global new_board
    for x in range(l):
        for y in range(l):
            new_board[y][l - x - 1] = board[r + x][c + y]

    for x in range(l):
        for y in range(l):
            board[r + x][c + y] = new_board[x][y]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check_ice(x, y):
    global board
    count = 0
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]

        if rx < 0 or ry < 0 or rx >= N or ry >= N: continue
        if board[rx][ry] == 0: continue
        count += 1

    if count < 3:
        return False
    else:
        return True


def bfs(x, y):
    global visited
    global board
    count = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        rx, ry = q.popleft()

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in range(4):
            tx = rx + dx[i]
            ty = ry + dy[i]
            if tx < 0 or ty < 0 or tx >= N or ty >= N: continue
            if visited[tx][ty] == 1 or board[tx][ty] == 0: continue
            count += 1
            visited[tx][ty] = 1
            q.append((tx, ty))

    return count


N, Q = map(int, input().split())
N = 2 ** N

board = [list(map(int, input().split())) for _ in range(N)]
L_list = list(map(int, input().split()))

for q in range(Q):
    l = 2 ** L_list[q]
    new_board = [[0] * l for _ in range(l)]
    for i in range(0, N, l):
        for j in range(0, N, l):
            rotate(i, j, l)

    decrease_points = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                if not check_ice(i, j):
                    decrease_points.append((i, j))

    for x, y in decrease_points:
        board[x][y] -= 1

mx = 0
visited = [[0] * N for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        result += board[i][j]
        if visited[i][j] == 0 and board[i][j] != 0:
            mx = max(mx, bfs(i, j))

print(result)
print(mx)
