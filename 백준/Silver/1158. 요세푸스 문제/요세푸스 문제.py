import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque(str(i) for i in range(N, 0, -1))
answer = list()

while queue:
    queue.rotate(K - 1)
    answer.append(queue.pop())

print("<" + ", ".join(answer) + ">")
