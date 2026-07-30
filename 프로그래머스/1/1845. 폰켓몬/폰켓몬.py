def solution(nums):
    poketmon = dict()
    for n in nums:
        poketmon[n] = poketmon.get(n, 0) + 1
    return min(len(poketmon), len(nums)//2)