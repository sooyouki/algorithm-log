import sys

N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    word = str(sys.stdin.readline().strip())
    c = set()
    is_groupword = True
    for i in range(len(word)):
        if i == 0:
            c.add(word[i])
            continue
        if word[i] != word[i - 1]:
            if word[i] not in c:
                c.add(word[i])
            else:
                is_groupword = False
                break
    if is_groupword:
        cnt += 1

print(cnt)
