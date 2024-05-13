import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start: int) -> list:
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
                
    return distance

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
    
distance_from_X = dijkstra(X)

result = 0
for node in range(1, N + 1):
    distance_to_X = dijkstra(node)[X]
    result = max(result, distance_to_X + distance_from_X[node])
    
print(result)