import sys

input = sys.stdin.readline

def DFS_row(x, y):
    if (-1 < x < N) and (-1 < y < M) and room[x][y] == '-' and not visited[x][y]:
        visited[x][y] = True
        DFS_row(x, y + 1)
        return True
    return False

def DFS_col(x, y):
    if (-1 < x < N) and (-1 < y < M) and room[x][y] == '|' and not visited[x][y]:
        visited[x][y] = True
        DFS_col(x + 1, y)
        return True
    return False


N, M = map(int, input().split())
room = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

count = 0
for r in range(N):
    for c in range(M):
        if DFS_row(r, c):
            count += 1
        if DFS_col(r, c):
            count += 1

print(count)