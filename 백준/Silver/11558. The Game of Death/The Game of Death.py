import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    graph = [0] + [int(input()) for _ in range(N)]

    cnt = 1
    p = graph[1]
    while p != N and cnt <= N:
        p = graph[p]
        cnt += 1

    print(0 if cnt > N else cnt)