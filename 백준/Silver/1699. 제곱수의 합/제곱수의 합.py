import sys, math

N = int(sys.stdin.readline())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = i
    limit = math.isqrt(i)

    if i == limit**2:
        dp[i] = 1

    for j in range(1, limit + 1):
        dp[i] = min(dp[i], 1 + dp[i - j**2])

print(dp[N])
