import sys

input = sys.stdin.readline

def DFS(graph, v, visited, cnt):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            cnt = DFS(graph, node, visited, cnt + 1)
    return cnt


N = int(input())
M = int(input())
graph = [[] for _ in range(1 + N)]
visited = [False] * (1 + N)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for connection in graph:
    connection.sort()

ans = DFS(graph, 1, visited, 0)
print(ans)