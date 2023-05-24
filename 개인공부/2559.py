import sys

input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))
 
temp = 0

for j in range(0,K) :
    temp += arr[j]
    
mx = temp

index_one = 1
index_two = index_one + K

while index_one <= N-K :
    temp = temp - arr[index_one-1] + arr[index_two-1]
    if mx < temp :
        mx = temp    
    index_one += 1
    index_two = index_one + K
    
print(mx)