import sys
import collections


def bfs(q, n, m):
    count = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        cur_x, cur_y = q[0]
        q.popleft()

        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]

            if 0 > new_x or 0 > new_y or new_x >= n or new_y >= m:
                continue
            if table[new_x][new_y] == 0 or visit[new_x][new_y] == True:
                continue
            q.append((new_x, new_y))
            visit[new_x][new_y] = True
            count += 1

    return count


n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[False] * m for i in range(n)]

count = 0
mx = 0
q = collections.deque()

for i in range(n):
    for j in range(m):
        if table[i][j] == 1 and visit[i][j] == False:
            q.append((i, j))
            visit[i][j] = True
            temp = bfs(q, n, m)
            count += 1
            mx = max(temp, mx)

print(count)
print(mx)
