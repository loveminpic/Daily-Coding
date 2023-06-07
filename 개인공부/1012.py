import sys
from collections import deque

input = sys.stdin.readline
T = int(input().strip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

for _ in range(T):
    M, N, K = map(int, input().strip().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    count = 0
    for _ in range(K):
        y, x = map(int, input().strip().split())
        arr[x][y] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                count += 1
    print(count)