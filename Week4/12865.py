import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * (K+1)
product = []

for i in range(0,N) :
    product.append(list(map(int, input().split())))

for i in range(0,N) :
    w,v = product[i]
    
    for j in range(K, w - 1, -1) :
        if arr[j-w] + v > arr[j] and i-j != j :
             arr[j] = arr[j-w] + v
        if j-w == j :
            if arr[j-w] > v :
                arr[w] = arr[j-w]     
print(arr[K])