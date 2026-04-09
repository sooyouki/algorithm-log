import sys, math

input = sys.stdin.readline

N = int(input())

cnt = 0


for c in str(math.factorial(N))[::-1]:
    if c == "0":
        cnt += 1
    else:
        break

print(cnt)
