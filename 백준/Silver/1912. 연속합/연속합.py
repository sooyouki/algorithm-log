import sys

N = int(sys.stdin.readline())

a = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = a[i]
    if dp[i - 1] > 0:
        dp[i] = a[i] + dp[i - 1]

print(max(dp[1:]))