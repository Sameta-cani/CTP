import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start: int, graph: list, distance: list) -> None:
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if distance[current_node] < current_distance:
            continue
        
        for adj, weight in graph[current_node]:
            distance_via_current = current_distance + weight
            if distance_via_current < distance[adj]:
                distance[adj] = distance_via_current
                heapq.heappush(priority_queue, (distance_via_current, adj))

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append((v, 1))
    
dijkstra(X, graph, distance)

k_distances = [idx for idx in range(1, N + 1) if distance[idx] == K]

print('\n'.join(map(str, k_distances)) if k_distances else -1)
    