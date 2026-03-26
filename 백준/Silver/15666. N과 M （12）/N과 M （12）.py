import sys


N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(set(map(int, sys.stdin.readline().split()))))
result = []


def dfs(start: int, selected: list[int]):
    if len(selected) == M:
        sequence = " ".join(map(str, selected))
        result.append(sequence)
        return

    for i in range(start, len(numbers)):
        dfs(i, selected + [numbers[i]])


dfs(0, [])
print(*result, sep="\n")
