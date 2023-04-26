import sys
input = sys.stdin.readline
from collections import deque

num = int(input().strip())
maze = [list(input().strip()) for _ in range(num)]

x = [1,0,-1,0]
y = [0,1,0,-1]

def bfs() :
    visited = [[-1] * num for _ in range(num)]
    visited[0][0] = 0
    queue = deque([[0,0]])
    
    while queue :
        r,c = queue.popleft()
        if [r, c] == [num-1, num-1] :
            return visited[num-1][num-1]
            
        for d in range(4) :
             dx = r + x[d]
             dy = c + y[d]
             if not (0 <= dx < num and 0 <= dy < num):
                continue
             if visited[dx][dy] == -1 :
                if maze[dx][dy] == '1' :
                    visited[dx][dy] = visited[r][c]
                    queue.appendleft([dx,dy])
                elif maze[dx][dy] == '0' :
                    visited[dx][dy] = visited[r][c] +1
                    queue.append([dx,dy])
                    


print(bfs())