import sys

n,m,v = map(int, sys.stdin.readline().split())

visted = [0] * (n+1)
node = [[] *(n+1) for _ in range(n+1)]
bfs = []
dfs = []

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
 
for i in range(0,n+1) :
    node[i].sort()

def bfs_f(v) : 
    visted[v] = 1
    bfs.append(v)
    queue = []
    queue.append(v)
   
    
    while queue :
        for i in node[queue.pop(0)] :
            if visted[i] == 0 :
                queue.append(i)
                bfs.append(i)
                visted[i] = 1
                
def dfs_f(v) :
    visted[v] = 1
    dfs.append(v)
    for i in node[v] :
        if visted[i] == 0 :
            dfs_f(i)

bfs_f(v)
print(bfs)
visted = [0] * (n+1)
dfs_f(v)
print(dfs)