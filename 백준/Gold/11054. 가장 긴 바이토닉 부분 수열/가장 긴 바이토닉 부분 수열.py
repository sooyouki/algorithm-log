import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = A[::-1]

dp_for = [0] * N
for i in range(N):
    dp_for[i] = 1
    for j in range(N):
        if A[i] > A[j] and dp_for[j] + 1 > dp_for[i]:
            dp_for[i] = dp_for[j] + 1

dp_back = [0] * N
for i in range(N):
    dp_back[i] = 1
    for j in range(N):
        if B[i] > B[j] and dp_back[j] + 1 > dp_back[i]:
            dp_back[i] = dp_back[j] + 1

dp = [(dp_for[i] + dp_back[N - i - 1] - 1) for i in range(N)]

print(max(dp))
