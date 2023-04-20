import sys
n,m,v = map(int, sys.stdin.readline().split())

location = [[] * (n+1) for _ in range(n+1)]
visted = [0] * (n + 1)
dfs = []
bfs = []
def dfs_f(index) :
    visted[index] = 1
    dfs.append(index)
    for i in location[index] :
        if visted[i] == 0 :
            dfs_f(i)

def bfs_f(index):
    visted[index] = 1
    bfs.append(index)
    queue = [index]
    while queue :
        for i in location[queue.pop(0)] :
            if visted[i] == 0 :
                queue.append(i)
                visted[i] = 1
                bfs.append(i)
                
for i in range(0, m) :
    a,b = map(int, sys.stdin.readline().split())
    location[a].append(b)
    location[b].append(a)
    
for j in range(0, n+1) :    
    location[j].sort() 

dfs_f(v)
visted = [0] * (n + 1)
bfs_f(v)

for i in dfs :
    print(i)
    
for i in bfs :
    print(i)
