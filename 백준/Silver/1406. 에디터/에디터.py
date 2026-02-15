import sys
from collections import deque

editor_left = deque(map(str, sys.stdin.readline().strip()))
editor_right = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "L":
        if editor_left:
            editor_right.appendleft(editor_left.pop())
    elif command[0] == "D":
        if editor_right:
            editor_left.append(editor_right.popleft())
    elif command[0] == "B":
        if editor_left:
            editor_left.pop()
    elif command[0] == "P":
        editor_left.append(command[1])

print("".join(editor_left + editor_right))
