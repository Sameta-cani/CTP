from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

def BFS(maps, N):
    queue = deque([(0, 0)])
    visited = [[False] * N for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        dist = maps[x][y]
        visited[x][y] = True

        for nx, ny in ((x + dist, y), (x, y + dist)):
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                return 'HaruHaru'
            queue.append((nx, ny))

    return 'Hing'

ans = BFS(maps, N)
print(ans)