import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = i
    if (i ** (1 / 2)).is_integer():
        dp[i] = 1
    for j in range(int(i ** (1 / 2)), 1, -1):
        dp[i] = min(dp[i], dp[j**2] + dp[i - j**2])

print(dp[N])
