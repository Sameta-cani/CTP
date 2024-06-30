from collections import deque
import sys

input = sys.stdin.readline

def topology_sort(V: int, indegree: list, graph: list) -> None:
    result = [] # List to store the topological sort
    q = deque() # Queue for processing nodes with 0 indegree
    
    # Init the queue with nodes having 0 indegree
    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)
            
    # Process the nodes until the queue is empty
    while q:
        node = q.popleft()
        result.append(node)
        
        # Decrease the indegree of adjacent nodes
        for adjacent in graph[node]:
            indegree[adjacent] -= 1
            # If indegree becomes 0, add the node to the queue
            if indegree[adjacent] == 0:
                q.append(adjacent)
                
    # Print the topological sort result
    print(' '.join(map(str, result)))
    
# Read number of nodes (V) and edges (E)
V, E = map(int, input().split())

# Init indegree array and adjacency list
indegree = [0] * (V + 1)
graph = [[] for _ in range(V + 1)]

# Read edges and populate graph and indegree array
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
# Perform topological sort
topology_sort(V, indegree, graph)