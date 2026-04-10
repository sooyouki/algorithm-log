import sys

input = sys.stdin.readline

N = int(input())
values = [list(map(int, input().split())) for i in range(N)]

rank = [1] * N
for i in range(N):
    for j in range(N):
        if values[i][0] < values[j][0] and values[i][1] < values[j][1]:
            rank[i] += 1

print(" ".join(map(str, rank)))
