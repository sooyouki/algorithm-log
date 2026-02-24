import sys

N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)
dp[1] = 1

for k in range(2, N + 1):
    dp[k] = 1
    for i in range(1, k + 1):
        if A[i] < A[k]:
            dp[k] = max(dp[k], dp[i] + 1)

print(max(dp))
