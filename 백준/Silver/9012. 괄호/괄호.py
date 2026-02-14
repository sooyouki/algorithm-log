import sys

N = int(sys.stdin.readline())

for _ in range(N):
    stack = []
    ps = sys.stdin.readline().strip()

    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            try:
                stack.pop()
            except IndexError:
                stack.append(p)
                break
    if not stack:
        print("YES")
    else:
        print("NO")
