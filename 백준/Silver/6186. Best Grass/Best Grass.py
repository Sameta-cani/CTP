import sys

input = sys.stdin.readline

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(graph: list, x: int, y: int) -> None:
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        
        if graph[cx][cy] == '#':
            graph[cx][cy] = ''
            
            for dx, dy in DIRECTIONS:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '#':
                    stack.append((nx, ny))


R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

result = 0
for r in range(R):
    for c in range(C):
        if graph[r][c] == "#":
            DFS(graph, r, c)
            result += 1
            
print(result)