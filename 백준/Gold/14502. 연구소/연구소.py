from collections import deque
from copy import deepcopy
import sys

def make_wall(count):
    if count == 3:
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                make_wall(count + 1)
                data[i][j] = 0

def BFS():
    queue = deque()
    temp = deepcopy(data)
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

    global result
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1

    result = max(result, count)


input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
make_wall(0)

print(result)