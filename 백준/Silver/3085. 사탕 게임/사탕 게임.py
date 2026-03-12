import sys

N = int(sys.stdin.readline())
board = list()
for _ in range(N):
    board.append(list(map(str, sys.stdin.readline().strip())))


def find_longest(board: list[str]):
    max_cnt = 1
    for i in range(N):
        # 가로
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    for j in range(N):
        # 세로
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt


result = 1
for i in range(N):
    for j in range(N):
        # 우측 swap
        if j + 1 < N and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            result = max(result, find_longest(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        # 아래측 swap
        if i + 1 < N and board[i][j] != board[i + 1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            result = max(result, find_longest(board))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(result)
