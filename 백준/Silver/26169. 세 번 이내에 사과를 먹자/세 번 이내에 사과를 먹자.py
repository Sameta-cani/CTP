import sys

input = sys.stdin.readline

N = 5

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(x, y, steps, apples):
    global found
    if apples >= 2:
        found = True
        return
    if steps == 3:
        return
    
    original = graph[x][y]
    graph[x][y] = -1
    
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != -1:
            DFS(nx, ny, steps + 1, apples + (1 if graph[nx][ny] == 1 else 0))
            
    graph[x][y] = original

graph = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())

found = False

DFS(R, C, 0, 0)

print(1 if found else 0)