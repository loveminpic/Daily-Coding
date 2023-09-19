import sys

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    temp = int(sys.stdin.readline().strip())
    arr.append(temp)

if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0] + arr[1])
else:
    dp = []
    dp.append(arr[0])
    dp.append(arr[0] + arr[1])
    case1 = max(arr[0] + arr[1], arr[1] + arr[2])
    case2 = max(case1, arr[0] + arr[2])
    dp.append(case2)

    for i in range(3, N):
        dp.append(max(dp[i - 1], dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]))
    print(dp[-1])
