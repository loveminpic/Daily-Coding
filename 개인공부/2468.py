import sys
import collections

input = sys.stdin.readline

N = int(input().strip())
graph = []
visited = [[False]* N for _ in range(N)]

mx = 0
mi = 10000000

for i in range(N):
    temp = list(map(int,input().split()))
    mx = max(mx,max(temp))
    mi = min(mi,min(temp))
    graph.append(temp)
    

def bfs(x,y,h) :
    visited[x][y] = True
    q = collections.deque()
    q.append((x,y))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while q :
        qx,qy = q.popleft()
        for i in range(4) :
            qdx = qx + dx[i]
            qdy = qy + dy[i]
            
            if qdx < 0 or qdx >= N or qdy < 0 or qdy >= N : continue
            if visited[qdx][qdy] == True or graph[qdx][qdy] <= h : continue
            q.append((qdx,qdy))
            visited[qdx][qdy] = True 

result = [1]

for h in range(mi,mx+1) :
    count = 0
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == False and graph[i][j] > h  :
                bfs(i,j,h)
                count += 1
    
    result.append(count)
    visited = [[False]* N for _ in range(N)]
    
print(max(result))