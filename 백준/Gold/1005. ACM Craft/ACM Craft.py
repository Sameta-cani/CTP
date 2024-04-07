from collections import deque
import copy
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    Delays = [0] + list(map(int, input().split()))

    indegree = [0] * (N + 1)

    graph = [[] for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    result = copy.deepcopy(Delays)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], Delays[i] + result[now])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    W = int(input())
    print(result[W])