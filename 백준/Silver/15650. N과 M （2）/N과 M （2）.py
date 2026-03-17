import sys

N, M = map(int, sys.stdin.readline().split())


def recursive(depth, numbers):
    if depth == M:
        print(*numbers)
        return
    for i in range(1, N + 1):
        if not numbers or i > numbers[-1]:
            numbers.append(i)
            recursive(depth + 1, numbers)
            numbers.pop()


recursive(0, [])
