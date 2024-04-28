def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, rank, a, b):
    rootA = find_parent(parent, a)
    rootB = find_parent(parent, b)
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
            if rank[rootA] == rank[rootB]:
                rank[rootB] += 1

def solution(n, computers):
    parent = list(range(n))
    rank = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):  # No need to check j < i, no need to include self-loops
            if computers[i][j] == 1:
                union_parent(parent, rank, i, j)
                
    # Find the number of unique roots
    unique_roots = len(set(find_parent(parent, i) for i in range(n)))
    return unique_roots