N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
groom = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]


def move(index):
    d = info[index][0]
    s = info[index][1]
    x = dx[d]
    y = dy[d]

    for i in range(len(groom)):
        r = groom[i][0]
        c = groom[i][1]

        r = (r + x * s + N) % N
        c = (c + y * s + N) % N

        new_groom.append((r, c))
        town[r][c] += 1


def magic():
    check = [2, 4, 6, 8]
    for i in range(len(new_groom)):
        r = new_groom[i][0]
        c = new_groom[i][1]
        count = 0
        for j in range(4):
            x = r + dx[check[j]]
            y = c + dy[check[j]]

            if x < 0 or y < 0 or x >= N or y >= N:
                continue
            if town[x][y] < 1: continue
            count += 1
        town[r][c] += count


def build_new():
    temp = []
    for i in range(N):
        for j in range(N):
            if town[i][j] >= 2:
                if (i, j) not in new_groom:
                    town[i][j] -= 2
                    temp.append((i, j))
    return temp


for i in range(M):
    new_groom = []
    move(i)
    magic()
    groom = build_new()

answer = 0
for m in town:
    answer += sum(m)

print(answer)
