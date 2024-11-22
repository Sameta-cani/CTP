import sys
input = sys.stdin.readline

N, M = map(int, input().split())
boards = [input().strip() for _ in range(N)]

def cal_repaints(x, y):
    w_cnt, b_cnt = 0, 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == 0:
                if boards[i][j] != 'W':
                    w_cnt += 1
                if boards[i][j] != 'B':
                    b_cnt += 1
            else:
                if boards[i][j] != 'B':
                    w_cnt += 1
                if boards[i][j] != 'W':
                    b_cnt += 1
    return min(w_cnt, b_cnt)

res = float('inf')
for n in range(N - 7):
    for m in range(M - 7):
        res = min(res, cal_repaints(n, m))

print(res)