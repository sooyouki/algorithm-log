import sys

E, S, M = 15, 28, 19
e, s, m = map(int, sys.stdin.readline().split())
e, s, m = e % E, s % S, m % M

num = 1
while True:
    if e == num % E and s == num % S and m == num % M:
        break
    num += 1

print(num)
