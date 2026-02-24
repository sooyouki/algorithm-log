import sys

N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [0] + [1] * 9

MOD = 1000000000

for k in range(2, N + 1):
    for i in range(10):
        dp[k][i] = ((dp[k - 1][i - 1] % MOD) if i > 0 else 0) + (
            (dp[k - 1][i + 1] % MOD) if i < 9 else 0
        )

print(sum(dp[N]) % MOD)
