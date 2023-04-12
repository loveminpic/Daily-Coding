import sys

num = int(input())
li = []
for i in range(0, num) :
    li.append(list(map(int,sys.stdin.readline().split())))

mx = []

for i in range(0, num) :
    mx.append(max(li[i]))
    
mxmx = max(mx)

