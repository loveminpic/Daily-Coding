import sys

def dfs(index) :
    visted[index] = True
    for i in nodes[index] :
        if visted[i] == False :
            dfs(i)
    
node, line = map(int, sys.stdin.readline().split())
visted = [False] * (node+1)

nodes = [[] for i in range(0,node+1)]

for i in range(0, line) :
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)
    
result = 0
for i in range(1,node+1) :
    if visted[i] == False :
        dfs(i)
        result += 1
        
print(result)