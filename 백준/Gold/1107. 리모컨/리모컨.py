import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(map(str, sys.stdin.readline().split()))
min_cnt = abs(N - 100)


for n in range(1000001):
    n_str = str(n)

    if any(k in broken for k in n_str):
        continue
    else:
        cnt = len(n_str) + abs(n - N)
        min_cnt = min(min_cnt, cnt)

print(min_cnt)
