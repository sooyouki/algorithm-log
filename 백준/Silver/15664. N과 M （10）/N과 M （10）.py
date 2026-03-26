import sys

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * N
result = []


def dfs(start: int, selected: list[int]):
    if len(selected) == M:
        result.append(" ".join(map(str, selected)))
        return

    prev = None

    for i in range(start, N):
        if visited[i]:
            continue
        if prev == numbers[i]:
            continue

        visited[i] = True
        dfs(i + 1, selected + [numbers[i]])
        visited[i] = False

        prev = numbers[i]


dfs(0, [])

print(*result, sep="\n")
