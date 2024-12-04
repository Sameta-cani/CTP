from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    visited = [False] * (N + 1)
    visited[start] = True

    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return visited

visited = dfs(1)

print(sum(visited) - 1)