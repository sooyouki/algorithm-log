import sys

N = int(sys.stdin.readline())

member = list()
for _ in range(N):
    input = sys.stdin.readline().split()
    member.append((int(input[0]), input[1]))

index = sorted(range(len(member)), key=lambda x: (member[x][0], x))

for i in index:
    print(*member[i])
