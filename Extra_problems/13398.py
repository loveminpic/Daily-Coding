import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 2 for i in range(N)]

dp[0][0] = arr[0]
dp[0][1] = arr[0]

for i in range(1, N):
    dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])

answer = -1000

for i in range(N):
    answer = max(answer, dp[i][0], dp[i][1])

print(answer)
