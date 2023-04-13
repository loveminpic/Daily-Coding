import sys

num = int(input())
li = []
for i in range(0, num) :
    li.append(list(map(int,sys.stdin.readline().split())))

mx = []

for i in range(0, num) :
    mx.append(max(li[i]))
    
mxmx = max(mx)
data = [[[0 for _ in range(num)] for _ in range(num)] for _ in range(mxmx)]

for h in range(0,mxmx) :
    for i in range(0,num) :
        for j in range(0, num):
            if li[i][j] <= h :
                data[h][i][j] = 1
            else :
                data[h][i][j] = 0
print(data)

dx = [1,0,-1,0]
dy = [0.1,0,-1]

s = []
output = []

for i in range(mxmx) :
    data[i][0][0] = 1
    s.append([0,0])
    
    while len(s) != 0 :
        count = 1
        x = s[-1][0]
        y = s[-1][1]
        s.pop(-1)
        
        for j in range(0,4) :
            if 
