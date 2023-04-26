import sys
sys.setrecursionlimit(10**6)

def dfs(index, current) :
    global check
    next = ""
    if check == False :
        return
    if color[index] == '0' :
        color[index] = current
        if current == 'A' :
            next = 'B'
        elif current == 'B' :
            next = 'A'
            
    for i in nodes[index] :
        if color[i] == '0': 
           dfs(i,next)
        else :
            if color[i] == current :
               check = False 
               break
           
          
            
if __name__ == '__main__':

    input = sys.stdin.readline

    num = int(input().strip())
    
        
    for i in range(0, num) :
        check = True
        a, b = map(int, input().split())
        nodes = [[]* (a+1) for i in range(0, a+1)]
        color = ['0'] * (a + 1)

        for j in range(0, b) :
            c, d =  map (int, input().split())
            nodes[c].append(d)
            nodes[d].append(c)
        
 
        for node in range(1, a + 1):
            if color[node] == '0':
                dfs(node, 'A')
           

        if check == True :
            print('YES')
        else :
            print('NO')   