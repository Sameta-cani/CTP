import sys
sys.setrecursionlimit(10 ** 6)

def dfs(graph, v, visited, count):
    visited[v] = count
    for i in graph[v]:
        if not visited[i]:
            count = dfs(graph, i, visited, count+1)
    return count

N, M, R = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for connections in graph:
    connections.sort()

dfs(graph, R, visited, 1)

for i in range(1, N+1):
    print(visited[i])