import sys

N = int(sys.stdin.readline())
min_n = float("inf")
max_n = float("-inf")
for n in map(int, sys.stdin.readline().split()):
    min_n = min(min_n, n)
    max_n = max(max_n, n)
   
print(min_n, max_n)