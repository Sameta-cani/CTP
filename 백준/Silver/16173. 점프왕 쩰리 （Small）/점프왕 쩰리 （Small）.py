from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    dist = maps[x][y]
    maps[x][y] = 101
    nx, ny = x + dist, y + dist
    if -1 < nx < N:
        queue.append((nx, y))
    if -1 < ny < N:
        queue.append((x, ny))

print('HaruHaru' if maps[N-1][N-1] == 101 else 'Hing')