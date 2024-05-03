from collections import deque
import sys

input = sys.stdin.readline

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    cnt = 0
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                cnt += 1

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

ans = BFS(graph, 1, visited)
print(ans)