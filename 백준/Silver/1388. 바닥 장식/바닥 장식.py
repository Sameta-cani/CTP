import sys

input = sys.stdin.readline

def DFS_row(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if not visited[x][y] and room[x][y] == '-':
        visited[x][y] = True
        DFS_row(x, y + 1)
        return True
    return False

def DFS_col(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if not visited[x][y] and room[x][y] == '|':
        visited[x][y] = True
        DFS_col(x + 1, y)
        return True
    return False

N, M = map(int, input().split())

room = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
for r in range(N):
    for c in range(M):
            if DFS_row(r, c):
                count += 1
            if DFS_col(r, c):
                count += 1

print(count)