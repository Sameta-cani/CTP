import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # Infinity represented by a large number

def dijkstra(start: int, graph: list, distance: list) -> None:
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if distance[current_node] < current_distance:
            continue
        
        for adjacent, weight in graph[current_node]:
            distance_via_current = current_distance + weight
            
            if distance_via_current < distance[adjacent]:
                distance[adjacent] = distance_via_current
                heapq.heappush(priority_queue, (distance_via_current, adjacent))
                
# Number of nodes and edges
N, M = map(int, input().split())
# Start node
start = int(input())
# Graph init
graph = [[] for _ in range(N + 1)]
# Distance table init
distance = [INF] * (N + 1)

# Edge information input
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
# Run Dijkstra's algorithm
dijkstra(start, graph, distance)

for idx in range(1, N + 1):
    if distance[idx] == INF:
        print("INFINITY")
    else:
        print(distance[idx])