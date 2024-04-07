import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    parent = list(range(N + 1))

    edges = []
    total = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    
    edges.sort()

    part_sum = 0
    for edge in edges:
        cost, a, b = edge
        total += cost
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            part_sum += cost
    
    print(total - part_sum)