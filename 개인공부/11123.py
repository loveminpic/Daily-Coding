import sys

input = sys.stdin.readline

case = int(input().strip())
col , row = map(int, input().split())

arr = []
visted = [[False] for _ in range()]
            
for i in range(case) :
    for j in range(col) :
        temp = input()
        temp2 = []
        for h in range(row) :
            temp2.append(temp[h])
        arr.append(temp2)
        
    for h in range(col) :
        for k in range(row) :
