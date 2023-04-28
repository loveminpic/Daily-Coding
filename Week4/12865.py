import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * (K+1)


for i in range(0,N) :
    W, V = map(int, input().split())

    for j in range(1, W) :
        if arr[j] > mx :
            mx = arr[j]
    arr[W] = mx

for i in range(K, 1, -1) :
    for j in range(1, i) :
        if arr[i - j] + arr[j] > arr[i] :
            arr[i] =  arr[i - j] + arr[j]
               
print(arr[K])
