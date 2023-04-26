import sys

computer_num = int(sys.stdin.readline().strip())
connection = int(sys.stdin.readline().strip())

nodes = [[] for i in range(0, computer_num+1)]

for i in range(0, connection) :
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)
    
visted = [False] * (computer_num+1)

def dfs(index) :
    visted[index] = True
    
    for i in nodes[index] :
        if visted[i] == False :
            dfs(i)
            

dfs(1)
count = 0
for i in visted :
    if i == True :
        count+= 1
        
        
print(count-1)
    