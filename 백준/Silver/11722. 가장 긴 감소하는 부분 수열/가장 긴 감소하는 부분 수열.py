import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[i] < A[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
