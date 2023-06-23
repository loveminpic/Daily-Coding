import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int,input().split()))
result = int(input().strip())

arr = sorted(arr)
a = 0
b = N-1
count = 0

while a < b :
    if arr[a]+ arr[b] == result :
        count += 1
        a += 1
        b -= 1
    elif arr[a] + arr[b] > result :
        b -= 1
    else :
        a += 1
print(count)
    

