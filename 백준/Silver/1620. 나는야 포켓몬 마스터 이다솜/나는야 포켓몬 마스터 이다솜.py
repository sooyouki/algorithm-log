import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
poketmon_dict_name = defaultdict()
poketmon_dict_num = defaultdict()

for i in range(1, N + 1):
    name = str(input().strip())
    poketmon_dict_name[name] = str(i)
    poketmon_dict_num[str(i)] = name

for _ in range(M):
    query = str(input().strip())
    if query.isdecimal():
        print(poketmon_dict_num[query])
    else:
        print(poketmon_dict_name[query])
