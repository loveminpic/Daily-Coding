import sys
input = sys.stdin.readline

num = int(input().strip())
arr = []
for i in range(num) :
    arr.append(int(input().strip()))
    
dp = [0] * num

if num == 1 :
    dp[0] = arr[0]
if num == 2 :
    dp[1] = arr[0] + arr[1]

for i in range(3,num) :
    dp[i]  = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+ dp[i-2], dp[-1])
        
print(dp[-1])