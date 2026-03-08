import sys, math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def isdecimal(a: int):
    if a == 1:
        return False

    for i in range(2, math.isqrt(a) + 1):
        if a % i == 0:
            return False
    return True


count = 0
for a in A:
    if isdecimal(a):
        count += 1

print(count)
