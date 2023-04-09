import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

data.sort()
for i in range (0,n) :
    
    print(data[i])
