import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N

for i in range(N):
    temp = 0
    for j in range(i):
        if A[i] > A[j]:
            temp = max(temp, dp[j])
    dp[i] = A[i] + temp

print(max(dp))