import sys

input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent: list, x: int) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent: list, a: int, b: int) -> None:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선(union 연산)의 개수 입력받기
V, E = map(int, input().split())
parent = list(range(V + 1))

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(E):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)