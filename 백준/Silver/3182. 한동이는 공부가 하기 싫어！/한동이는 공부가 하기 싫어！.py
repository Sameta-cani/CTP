import sys
input = sys.stdin.readline


def DFS(graph, v, visited, cnt):
    visited[v] = True
    for node in [graph[v]]:
        if not visited[node]:
            cnt = DFS(graph, node, visited, cnt + 1)
    return cnt


N = int(input())
graph = [0] + [int(input()) for _ in range(N)]

max_value = 0
best_node = 0

for idx in range(1, N + 1):
    visited = [False] * (N + 1)
    res = DFS(graph, idx, visited, 0)
    if res > max_value:
        max_value = res
        best_node = idx

print(best_node)