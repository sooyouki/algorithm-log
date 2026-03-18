import sys

N, M = map(int, sys.stdin.readline().split())


def dfs(start: int, depth: int, selected: list[int]):
    if depth == M:
        print(*selected)
        return

    for n in range(start, N + 1):
        selected.append(n)
        dfs(start, depth + 1, selected)
        selected.pop()


dfs(1, 0, [])
