import sys

N = int(sys.stdin.readline().strip())
nums = []
stack = []
answer = []

for _ in range(N):
    a = int(sys.stdin.readline().strip())
    nums.append(a)

idx = 0
for i in range(1, N + 1):
    stack.append(i)
    answer.append("+")
    while stack and stack[-1] == nums[idx]:
        stack.pop()
        answer.append("-")
        idx = idx + 1

if len(answer) != 2 * N:
    print("NO")
else:
    print("\n".join(answer))
