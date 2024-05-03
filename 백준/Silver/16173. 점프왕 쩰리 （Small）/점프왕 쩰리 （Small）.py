import sys

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def DFS(x, y):
    visited[x][y] = True
    dist = maps[x][y]

    for nx, ny in ((x + dist, y), (x, y + dist)):
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            DFS(nx, ny)

DFS(0, 0)

if visited[N - 1][N - 1]:
    print('HaruHaru')
else:
    print('Hing')