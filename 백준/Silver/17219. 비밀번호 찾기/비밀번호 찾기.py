import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
store = defaultdict()

for _ in range(N):
    domain, password = input().split()
    store[domain] = password

for _ in range(M):
    domain = input().strip()
    print(store[domain])
