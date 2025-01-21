import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

stack = [(0, 0)]

is_cond = False
while stack:
    cx, cy = stack.pop()
    dist = graph[cx][cy]
    
    if dist == -1:
        is_cond = True
        break
    
    if not visited[cx][cy]:
        visited[cx][cy] = True
        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = cx + dist * dx, cy + dist * dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                stack.append((nx, ny))
            
print("HaruHaru" if is_cond else "Hing")