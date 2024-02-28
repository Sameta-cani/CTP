def dfs(graph, v, visited, depth):
    visited[v] = depth
    for i in graph[v]:
        if visited[i] == -1:
            dfs(graph, i, visited, depth+1)

N = int(input())
target_u, target_v = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for connections in graph:
    connections.sort()

dfs(graph, target_u, visited, 0)

print(visited[target_v])