import sys

num = int(sys.stdin.readline().strip())
arr = []

for i in range(num) :
    arr.append(int(sys.stdin.readline().strip()))

if num == 1:
    print(arr[0])

elif num == 2:
    print(arr[0] + arr[1])
    
else :
    dp = []     

    dp.append(arr[0])
    dp.append(arr[0]+arr[1])
    dp.append(max(arr[0]+arr[2], arr[1]+ arr[2]))

    for i in range(3, num) :
        dp.append(max(dp[i-2]+arr[i], arr[i-1]+arr[i]+dp[i-3]))
        
    print(dp[-1])