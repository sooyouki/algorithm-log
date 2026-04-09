import sys
from itertools import combinations

input = sys.stdin.readline

for line in sys.stdin:
    if line == "0":
        break

    attributions = line.split()
    K, S = attributions[0], attributions[1:]

    for c in combinations(S, 6):
        print(" ".join(map(str, c)))

    print()
