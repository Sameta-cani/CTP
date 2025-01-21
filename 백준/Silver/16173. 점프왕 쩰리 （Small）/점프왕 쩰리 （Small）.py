import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

cond = False

stack = [(0, 0)]
while stack:
    x, y = stack.pop()
    dist = graph[x][y]
    
    if dist == -1:
        cond = True
        break
    
    if not visited[x][y]:
        visited[x][y] = True
        
        for dx, dy in [(1, 0), (0, 1)]:
            nx, ny = x + dist * dx, y + dist * dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                stack.append((nx, ny))
                
print("HaruHaru" if cond else "Hing")