import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums == [0, 0, 0]:
        exit()

    nums.sort()
    if nums[2] ** 2 == nums[1] ** 2 + nums[0] ** 2:
        print("right")
    else:
        print("wrong")
