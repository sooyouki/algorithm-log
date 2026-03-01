import sys

N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0, 0] for _ in range(N + 1)]

for k in range(1, N + 1):
    dp[k][0] = 1
    dp[k][1] = k
    for i in range(1, k):
        if A[k] > A[i] and dp[k][0] <= dp[i][0]:
            dp[k][0] = dp[i][0] + 1
            dp[k][1] = i

max_idx = 0
for idx, n in enumerate(dp):
    if dp[idx] > dp[max_idx]:
        max_idx = idx

path = [A[max_idx]]
route = max_idx
while True:
    if route == dp[route][1]:
        break
    route = dp[route][1]
    path.append(A[route])

print(dp[max_idx][0])
print(*path[::-1])
