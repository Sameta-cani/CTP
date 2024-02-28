import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N = int(input())
num_of_pairs = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(num_of_pairs):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for connections in graph:
    connections.sort()

dfs(graph, 1, visited)

print(sum(visited[2:]))