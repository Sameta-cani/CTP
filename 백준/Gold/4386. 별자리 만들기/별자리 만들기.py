import sys
import math

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

N = int(input())
parent = list(range(N + 1))

edges = []
result = 0

stars = []

for i in range(1, N + 1):
    x, y = map(float, input().split())
    stars.append((x, y, i))

stars.sort()

for i in range(N):
    for j in range(i, N):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), stars[i][2] ,stars[j][2]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(f'{result:.2f}')