import sys

N = int(sys.stdin.readline())
len_N = len(str(N))

cnt = 0

for i in range(1, len_N):
    cnt += 9 * (10 ** (i - 1)) * i

cnt += (N - 10 ** (len_N - 1) + 1) * len_N

print(cnt)
