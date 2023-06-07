import sys

N = int(sys.stdin.readline().strip())
A = []

for i in range(N) :
    A.append([i, int(sys.stdin.readline().strip())])

check = sorted(A,key=lambda x:x[1])
print(check)
m = 0

for i in range(N) :
    temp = check[i][0] - i 
    m = max(m, temp)
        
print(m+1)
