import sys

board = [[0] * 100 for _ in range(100)]

N = int(sys.stdin.readline().rstrip())
result = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    x, y = x-1, y-1
    for i in range(10):
        for j in range(10):
            if board[y+i][x+j] == 0:
                board[y+i][x+j] = 1
                result += 1

print(result)