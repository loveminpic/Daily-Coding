import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input().strip())

arr = []
arr2 = [] 
visted = [[False]* N for _ in range(N)]

for i in range(N):
    temp = input().split()
    temp2 = []
    temp3 = []
    for h in range(N) :
        if temp[0][h] == "G" :
            temp3.append("R")
        else :
            temp3.append(temp[0][h])
            
        temp2.append(temp[0][h])
        
            
    arr.append(temp2)
    arr2.append(temp3)
    
def dfs(arr,x,y,col) :
    visted[x][y] = True
    
    x1 = [0,-1,0,1]
    y1 = [1,0,-1,0]
    
    for j in range(0,4) :
        dx = x + x1[j]
        dy = y + y1[j]
        
        if dx < 0 or dy < 0 or dx >= N or dy >= N : continue
        if visted == True or arr[dx][dy] != col : continue
        if arr[dx][dy] == col and visted[dx][dy] == False :
            dfs(arr,dx,dy,col)
            
count = 0
for i in range(N) :
    for j in range(N) :
        if visted[i][j] == False :
            col = arr[i][j] 
            dfs(arr,i,j,col)
            count += 1
    
result = []
result.append(count)

count = 0 
visted =  [[False]* N for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if visted[i][j] == False :
            col = arr2[i][j] 
            dfs(arr2,i,j,col)
            count += 1
              
result.append(count)

[print(*result)]
