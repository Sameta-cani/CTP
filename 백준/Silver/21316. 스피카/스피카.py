from collections import deque
import sys
input = sys.stdin.readline

def BFS(graph, start):
    queue = deque([(start, 0)])
    visited = [False] * len(graph)
    visited[start] = True
    level_count = 0

    while queue:
        now, level = queue.popleft()
        if level == 2:
            level_count += 1
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                queue.append((node, level + 1))

    return level_count

graph = [[] * 13 for _ in range(13)]
for _ in range(12):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for idx in range(1, 13):
    if len(graph[idx]) == 3:
        res = BFS(graph, idx)
        if res + 3 == 6:
            print(idx)
            break