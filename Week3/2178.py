import sys
import collections
input = sys.stdin.readline

N,M = map(int, input().split())
node = []

count = 0
for i in range(0, N):
    point = input().strip()  # 공백을 제거한 문자열로 입력 받음
    point_list = [int(char) for char in point]  # 문자열의 각 문자를 정수로 변환하여 리스트로 만듦
    node.append(point_list)
    
queue = collections.deque()
queue.append([0,0])

x = [0,1,0,-1]
y = [1,0,-1,0]

while queue :
    qx,qy = queue.popleft()
    
    for i in range(0,4) :
        dx = x[i] + qx
        dy = y[i] + qy
        
        if dx < 0 or dy < 0 or dx >= N or dy >= M : continue
        if node[dx][dy] != 1 : continue
        queue.append([dx,dy])
        node[dx][dy] = node[qx][qy] + 1

print(node[N-1][M-1])
                      