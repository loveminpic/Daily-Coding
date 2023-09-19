import sys

N = int(sys.stdin.readline().strip())
plan = []
dp = []

plan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0] * (N + 1)


for i in range(N):
    dp[i] = max(dp[i], dp[i - 1])
    idx = i
    while idx + plan[idx][0] <= N:
        dp[idx + plan[idx][0]] = max(
            dp[idx + plan[idx][0]],
        )
        idx += plan[i][0]


print(max(dp))
