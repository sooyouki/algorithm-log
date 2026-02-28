import sys

N = int(sys.stdin.readline())

cost = [[0] * 3]
dp = [[0] * 3 for _ in range(N + 1)]

for _ in range(N):
    input = list(map(int, sys.stdin.readline().split()))
    cost.append(input)

for i in range(1, N + 1):
    dp[i] = [
        cost[i][0] + min(dp[i - 1][1], dp[i - 1][2]),
        cost[i][1] + min(dp[i - 1][0], dp[i - 1][2]),
        cost[i][2] + min(dp[i - 1][0], dp[i - 1][1]),
    ]

print(min(dp[N]))
