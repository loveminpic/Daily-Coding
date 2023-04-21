import sys
import collections
input = sys.stdin.readline


M, N, H = map (int, input().split())

min_list = []
queue = collections.deque()
    
visted = [[] * H for _ in range(0,H)]

for i in range(0, H) :
    for j in range(0, N):
        location = list(map(int,sys.stdin.readline().split()))
        visted[i].append(location)
    
for i in range(0, H) :
    # 처음 queue에 값넣기
    for j in range(0,N) :
        for h in range(0,M) :
            if visted[i][j][h] == 1 :
                queue.append([j,h])
                break
        if len(queue) != 0 :
            break

    x = [0,1,0,-1]
    y = [1,0,-1,0]

    while queue :
        qx, qy = queue.popleft()
        for j in range(0,4) :
            dx = qx + x[j]
            dy = qy + y[j]
            if dx < 0 or dy < 0 or dx >= N or dy >= M : continue
            if visted[i][dx][dy] != 0 :
                continue
            queue.append([dx,dy])
            visted[i][dx][dy] = visted[i][qx][qy] + 1
                

