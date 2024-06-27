import heapq
import sys
from typing import List, Tuple

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start: int, graph: List[List[Tuple[int, int]]], distance: List[int]) -> None:
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
                
# Number of nodes, edges, and start node
N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

# Input edges
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
dijkstra(start, graph, distance)

# Calculate the number of reachable nodes and the maximum distance
reachable_nodes = [d for d in distance if d != INF]
count = len(reachable_nodes) - 1 # Exclude the start node
max_distance = max(reachable_nodes, default=0)

print(count, max_distance)