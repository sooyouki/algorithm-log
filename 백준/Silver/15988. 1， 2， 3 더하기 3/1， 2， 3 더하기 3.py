import sys

T = int(sys.stdin.readline())
ns = list(map(int, sys.stdin.readlines()))

N = 1000000
MOD = 1000000009

dp = [0] * (N + 1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, N + 1):
    dp[i] = (dp[i - 1] % MOD + dp[i - 2] % MOD + dp[i - 3] % MOD) % MOD

for n in ns:
    print(dp[n])
