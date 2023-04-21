import sys
import collections
import copy
input = sys.stdin.readline

R,C = map(int, input().split())
node = [[] * (R) for _ in range(R)]
water_node = [[0] * (R) for _ in range(R)]

queue = collections.deque()
queue_for_water = collections.deque()
a = 0
b = 0

for i in range(0,R) :
    temp = input().strip()
    for j in range(0,len(temp)) :
        if temp[j] == 'D':
            node[i].append('D')
            a = i
            b = j
        elif temp[j] == '.' :
            node[i].append(0)
        elif temp[j] == '*' :
            node[i].append(1)
            queue_for_water.append([i,j])
        elif temp[j] == 'X' :
            node[i].append(temp[j])
        elif temp[j] == 'S' :
            node[i].append(0)
            c = i
            d = j
            queue.append([i,j])

water_node = copy.deepcopy(node)
 
      
x = [0,-1,0,1]
y = [1,0,-1,0]

found = False

while len(queue) > 0  :
    if found :
        break
    
    water_size = len(queue_for_water)
    for _ in range(water_size) :
        qwx, qwy = queue_for_water.popleft()
        
        for j in range(0,4) :
            dx = qwx + x[j]
            dy = qwy + y[j]
            
            if dx < 0 or dy < 0 or dx >= R or dy >= C : continue
            if water_node[dx][dy] == 1 or water_node[dx][dy] == 'X' or water_node[dx][dy] == 'D' : continue
            queue_for_water.append([dx,dy])
            water_node[dx][dy] = 1
    
    lee_size = len(queue)
    for _ in range(lee_size) :
        mr_lee_x, mr_lee_y = queue.popleft()

        for j in range(0,4) :
            mdx = mr_lee_x + x[j]
            mdy = mr_lee_y + y[j]
            
            if mdx < 0 or mdy < 0 or mdx >= R or mdy >= C : continue
            if water_node[mdx][mdy] == 1 or water_node[mdx][mdy] == 'X' or [mdx,mdy] == [c,d] : continue
            if node[mdx][mdy] == 'D':
                found = True
                node[mdx][mdy] = node[mr_lee_x][mr_lee_y] + 1
                break
            if node[mdx][mdy] == 0:
                queue.append([mdx,mdy])
                node[mdx][mdy] = node[mr_lee_x][mr_lee_y] + 1


if node[a][b] == 'D':
    print("KAKTUS")
else:
    print(node[a][b])