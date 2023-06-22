import sys

input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

arr = []
for i in range(1,N+1) :
    for j in range(1, N+1) :
        arr.append(i*j)
        
arr = sorted(arr)
print(arr[K])