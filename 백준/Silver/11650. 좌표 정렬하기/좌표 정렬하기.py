import sys
input = sys.stdin.readline

points = [tuple(map(int, input().split())) for _ in range(int(input()))]

points.sort(key=lambda x: [x[0], [x[1]]])

for point in points:
    print(*point)