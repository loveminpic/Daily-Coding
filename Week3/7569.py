import sys
import collections
input = sys.stdin.readline

# 인풋 받고
M, N, H = map (int, input().split())

# 필요한 배열 만들어주기, 큐, visted, mx 값
queue = collections.deque()
visted = [[] * H for _ in range(0,H)]
mx = 1

# 문제에 주어지는 배열을 다 담아줌 
for i in range(0, H) :
    for j in range(0, N):
        location = list(map(int,input().split()))
        visted[i].append(location)

# 그리고 익은 토마토가 있는 모든 위치를 큐에 담아줌
for i in range(0, H) :
    for j in range(0,N) :
        for h in range(0,M) :
            if visted[i][j][h] == 1 :
                queue.append([i,j,h])

# 상하좌우 좌표위치를 설정
x = [0,1,0,-1,0,0]
y = [1,0,-1,0,0,0]
z = [0,0,0,0,1,-1]

# 이제 큐가 빌때까지 열심히 상하좌우로 
while queue :
    qz, qx, qy = queue.popleft()
    
    for j in range(0,6) :
        dz = qz + z[j]
        dx = qx + x[j]
        dy = qy + y[j]
        # 상하좌우가 배열을 벗어나는지 확인
        if dx < 0 or dy < 0 or dz < 0 or dx >= N or dy >= M or dz >= H: continue
        # 이미 방문한 곳인지 확인
        if visted[dz][dx][dy] != 0 :
            continue
        # 위의 조건을 둘다 만족하지 않으면, 큐에 넣음
        queue.append([dz,dx,dy])
        # 방문했다고도 표신 그 대신 몇일차에 왔는지.. 확인 
        visted[dz][dx][dy] = visted[qz][qx][qy] + 1
        # 미리 가장 큰 값을 확인
        mx = max(mx,visted[dz][dx][dy])

check = True
for i in range(0, H) :
    for j in range(0,N) :
        for h in range(0,M) :
            if visted[i][j][h] == 0 :
                check = False
                break
        if check == False :
            break
    if check == False :
        break
    
if check == True :
    print(mx-1)
else :
    print(-1)