import sys

people = 2
ch = 1
arr = []

input = sys.stdin.readline
N = int(input().strip())

for i in range(N) :
    arr.append([people, ch])
    temp1 = people
    temp2 = ch
    ch = temp1
    people = temp1 + temp2
     
result = [[] * N]

for i in range(2, N) :
    if N % i == 0 :
        result[i].append(arr[i]*(N//i))
    else :
        for j in range(i,N):
            

            
mi = min(result)
mx = max(result)
print(mi, mx)

