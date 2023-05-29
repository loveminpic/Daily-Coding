import sys
import collections

input = sys.stdin.readline

N,M = map(int, input().split())
arr =  collections.deque()


for i in range(1, N+1) :
    arr.append(i)
    
q = list(map(int,input().split()))
    
count  = 0

for i in range(M) :
    if arr[0] == q[i] :
        arr.popleft()
    else :
        while arr[0] != q[i] :
            if arr.index(q[i]) < len(arr)/2 :
                arr.rotate(-1)
                count += 1
            else :
                arr.rotate()
                count += 1 
        arr.popleft()
            
            
                 
print(count)