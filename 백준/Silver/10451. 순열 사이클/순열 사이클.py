import sys

input = sys.stdin.readline

def DFS(graph, v, visited):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            DFS(graph, node, visited)

for _ in range(int(input())):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for idx in range(1, N + 1):
        graph[idx].append(data[idx])
    res = 0
    for idx in range(1, N + 1):
        if not visited[idx]:
            res += 1
            DFS(graph, idx, visited)
    print(res)
    