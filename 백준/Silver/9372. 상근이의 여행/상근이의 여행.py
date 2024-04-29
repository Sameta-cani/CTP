import sys

input = sys.stdin.readline

def DFS(graph, v, visited, cnt):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            cnt = DFS(graph, node, visited, cnt + 1)
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(1 + N)]
    visited = [False] * (1 + N)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    count = DFS(graph, 1, visited, 0)
    print(count)