from collections import deque
import sys

input = sys.stdin.readline

# Number of nodes
v = int(input())
# Init indegree and graph
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
# Init time array
time = [0] * (v + 1)

# Read graph information
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for prerequisite in data[1:-1]:
        indegree[i] += 1
        graph[prerequisite].append(i)
        
# Topological sort function
def topology_sort() -> None:
    result = time[:] # Copy initial times to result
    q = deque()
    
    # Enqueue nodes with no incoming edges
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            
    # Process the queue
    while q:
        node = q.popleft()
        for adjacent in graph[node]:
            result[adjacent] = max(result[adjacent], result[node] + time[adjacent])
            indegree[adjacent] -= 1
            if indegree[adjacent] == 0:
                q.append(adjacent)
                
    # Print the result times
    for i in range(1, v + 1):
        print(result[i])
        
# Excute the topological sort
topology_sort()