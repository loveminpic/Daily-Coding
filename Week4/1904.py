import sys

num = int(sys.stdin.readline().strip())

arr = [0] * 1000001
arr[1] = 1
arr[2] = 2
arr[3] = 3

for i in range(4,num+1):
    arr[i] = arr[i-1] + arr[i-2]
    if arr[i] >= 15746 :
        arr[i] = arr[i] % 15746
        
print(arr[i])