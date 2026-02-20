import sys
from collections import deque


def solution(start):
    queue = deque([(start, 0)])
    visited = [False] * (start + 1)
    visited[start] = True

    while queue:
        n, depth = queue.popleft()

        if n == 1:
            return depth

        for next_n in (
            n // 3 if (n % 3 == 0) else n,
            n // 2 if (n % 2 == 0) else n,
            n - 1,
        ):
            if not visited[next_n]:
                visited[next_n] = True
                queue.append((next_n, depth + 1))

    return -1


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print(solution(n))
