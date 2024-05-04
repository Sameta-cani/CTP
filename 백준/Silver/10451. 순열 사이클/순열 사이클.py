import sys

input = sys.stdin.readline

def DFS(graph, v, visited):
    stack = [v]
    while stack:
        now = stack.pop()
        visited[now] = True
        for next_node in graph[now]:
            if not visited[next_node]:
                stack.append(next_node)

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