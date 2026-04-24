import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(int(input()) for _ in range(N))
cnt = 0
prev = len(A) - 1
while K > 0:
    for i in range(prev, -1, -1):
        if A[i] <= K:
            cnt += K // A[i]
            K %= A[i]
            prev = i
            break

print(cnt)
