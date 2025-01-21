from collections import deque
import sys

input = sys.stdin.readline

N = 10  # Grid size

# Parse input and locate 'B' and 'L'
graph = []
start = None
for i in range(N):
    row = list(input().strip())
    graph.append(row)
    if 'B' in row:
        start = (i, row.index('B'))

# BFS directions (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS to find the shortest path from 'B' to 'L'
def bfs_shortest_path(graph, start):
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, dist = queue.popleft()
        
        # If we reach 'L', return the distance (excluding start point)
        if graph[x][y] == 'L':
            return dist - 1  # Exclude start and end points
        
        # Explore neighbors
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if graph[nx][ny] in {'.', 'L'}:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
    
    return -1  # Return -1 if no path exists

# Calculate and print the result
result = bfs_shortest_path(graph, start)
print(result)
