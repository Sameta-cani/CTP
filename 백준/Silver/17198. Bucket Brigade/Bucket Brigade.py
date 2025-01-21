from collections import deque
import sys

input = sys.stdin.readline

N = 10

graph = []
start = None
for idx in range(N):
    row = list(input().strip())
    graph.append(row)
    if 'B' in row:
        start = (idx, row.index('B'))
        
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque([(start[0], start[1], 0)])
visited = set()
visited.add(start)

res = 0
while queue:
    x, y, dist = queue.popleft()
    
    if graph[x][y] == 'L':
        res = dist - 1
        break
    
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
            if graph[nx][ny] != 'R':
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
                
print(res)