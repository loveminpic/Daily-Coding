import sys 

num = int(sys.stdin.readline().strip())
nodes = [[] * (num+1) for i in range(num+1)]
parent = [0] * (num + 1)
vis = [0] * (num + 1)

for i in range(num-1) :
    a,b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)
    

# def dfs (index) :
#    vis[index] = 1 
#    for i in nodes[index] :
#        if vis[i] == 0 and parent[i] == 0:
#            parent[i] = index
#            dfs(i)
        

def dfs(index) :
    stack = [index]
    vis[index] = 1
    
    while stack :
        current = stack.pop()
        
        for i in nodes[parent] :
            if vis[i] == 0 and parent[i] == 0 :
                parent[i] = current
                vis[i] == 1
                stack.ap
                
dfs(1)

for i in range(2,len(parent)) :
    print(parent[i])

