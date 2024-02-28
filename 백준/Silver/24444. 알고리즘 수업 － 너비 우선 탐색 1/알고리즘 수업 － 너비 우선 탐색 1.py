from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)


def bfs(graph, start, visited):
    order = 1
    queue = deque([start])
    visited[start] = order
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                order += 1
                queue.append(i)
                visited[i] = order

N, M, R = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for connections in graph:
    connections.sort()

bfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])