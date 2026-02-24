import sys

T = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readlines()))

N = max(n)
MOD = 1000000009

dp = [[0] * 3 for _ in range(N + 1)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for k in range(4, N + 1):
    dp[k][0] = (dp[k - 1][1] + dp[k - 1][2]) % MOD
    dp[k][1] = (dp[k - 2][0] + dp[k - 2][2]) % MOD
    dp[k][2] = (dp[k - 3][0] + dp[k - 3][1]) % MOD

for i in n:
    print(sum(dp[i]) % MOD)
