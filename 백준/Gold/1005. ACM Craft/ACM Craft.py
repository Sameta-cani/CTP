from collections import deque
import copy
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    Delays = list(map(int, input().split()))
    cost = 0

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
            cost += Delays[i - 1]

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i - 1] = max(result[i - 1], Delays[i - 1] + result[now - 1])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    W = int(input())
    print(result[W - 1])