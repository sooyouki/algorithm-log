import sys

n = int(sys.stdin.readline())
amount = list()
for _ in range(n):
    amount.append(int(sys.stdin.readline()))

dp = [[0] * 3 for _ in range(n)]
dp[0] = [amount[0], amount[0], 0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][1] + amount[i]
    dp[i][1] = dp[i - 1][2] + amount[i]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])

print(max(dp[n - 1]))