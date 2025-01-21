import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
cnt = -1
stack = [1]
while stack:
    v = stack.pop()
    
    if not visited[v]:
        visited[v] = True
        cnt += 1
        
        stack.extend(node for node in graph[v] if not visited[node])
        
print(cnt)