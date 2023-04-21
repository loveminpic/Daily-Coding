import sys
import collections
input = sys.stdin.readline

N,M,K,X = map(int, input().split())

node = [[] * (N+1) for _ in range(0,N+1)]


visted = [0] * (N+1)
queue = collections.deque()

for i in range(0,M):
    a, b = list(map(int, input().split()))
    node[a].append(b)

queue.append(X)
visted[X] = 1

while queue :
    temp = queue.popleft()
    for i in node[temp] :
        if visted[i] == 0 :
            queue.append(i)
            visted[i] = visted[temp] + 1
            
check = True
for i in range(0,N+1) :
    if visted[i] - 1 == K :
        print(i)
        check = False

if check == True :
    print(-1)
