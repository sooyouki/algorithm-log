import sys

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
result = []


def dfs(selected: list[int]):
    if len(selected) == M:
        result.append(" ".join(map(str, selected)))
        return

    for n in numbers:
        selected.append(n)
        dfs(selected)
        selected.pop()


dfs([])

print(*result, sep="\n")
