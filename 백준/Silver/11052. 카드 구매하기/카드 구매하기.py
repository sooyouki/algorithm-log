import sys

N = int(sys.stdin.readline())
p = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)
dp[1] = 1

for k in range(1, N + 1):
    dp[k] = max((dp[k - i] + p[i]) for i in range(1, k + 1))

print(dp[N])
