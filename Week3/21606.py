import sys

def dfs(index,count) :
    visited[index] = True
    for i in nodes[index] :
        if out_in[i-1] == 1 and visited[i] == False :
            count += 1
        elif out_in[i-1] == 0 and visited[i] == False :
            count = dfs(i,count)
    return count
    
            
if __name__ == '__main__':

    input = sys.stdin.readline
    num = int(input().strip())
    
    temp = input().strip()
    out_in = [int(i) for i in temp]

    nodes = [[] * (num+1) for i in range(num+1)]
    for i in range(1,num):
        a, b = map(int,input().split())
        nodes[a].append(b)
        nodes[b].append(a)
        
    all_count = 0 
    
    for j in range(1, num+1):
        count = 0
        if out_in[j-1] == 1 :
            visited = [False] * (num+1)
            all_count += dfs(j, count)
    
    print(all_count)