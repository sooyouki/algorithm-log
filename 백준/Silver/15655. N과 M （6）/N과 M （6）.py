import sys
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
result = []


def dfs(start: int, depth: int, selected: list[int]):
    if depth == M:
        result.append(" ".join(map(str, selected)))
        return

    for i, n in enumerate(numbers[start : N + 1]):
        if n not in selected:
            selected.append(n)
            dfs(start + i + 1, depth + 1, selected)
            selected.pop()


dfs(0, 0, [])

print(*result, sep="\n")
