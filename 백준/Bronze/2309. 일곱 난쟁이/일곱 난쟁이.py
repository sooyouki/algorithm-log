import sys

height = list()
for _ in range(9):
    height.append(int(sys.stdin.readline()))
height.sort()

value = sum(height) - 100

for i in range(9):
    for j in range(i + 1, 9):
        if value == height[i] + height[j]:
            del height[j]
            del height[i]
            for h in height:
                print(h)
            exit()
