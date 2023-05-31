import sys

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))
    
arr = sorted(arr)
count = 0
mx = 0
for i in range(N) :
    mx = max(mx , (N - count) * arr[i])
    count += 1
    
print(mx)