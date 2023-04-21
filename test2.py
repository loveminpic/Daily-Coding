import sys

n,m,v = map(int(sys.stdin.readline().split()))

node = [[] * (n+1) for _ in range(0, n+1)]
visted = [] * (n+1)
dfs = []
bfs = []

for i in range(0,n+1) :
    a, b = map(int, sys.stdin.readline().split())
    node[a].append = b
    node[b].append = a
    
for j in range(0, n+1) :    
    node[j].sort() 

def dfs_f(v) :
    visted[v] = 1
    dfs.append(v)
    for i in node[v] :
        if visted[i] == 0 :
            dfs_f(i)

def bfs_f(v) :
    visted[v] = 1
    bfs.append(v)
    queue = []
    while queue :
        for i in visted[queue.pop(0)] :
            if visted[i] == 0 :
                bfs.append(i)
                queue.append(i)
                visted[i] = 1
                
    

        
    
    
        