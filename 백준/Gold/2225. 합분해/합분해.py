import sys, math

N, K = list(map(int, sys.stdin.readline().split()))
MOD = 1000000000

h = [math.comb(K, t) for t in range(K + 1)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][1] = 1
    for j in range(2, K + 1):
        dp[i][j] = sum(dp[k][j - 1] % MOD for k in range(1, i)) % MOD

print(sum([(dp[N][i] * h[i]) % MOD for i in range(K + 1)]) % MOD)