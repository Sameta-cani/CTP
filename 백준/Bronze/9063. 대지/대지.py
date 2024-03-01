N = int(input())
x_min, x_max = float('inf'), float('-inf')
y_min, y_max = float('inf'), float('-inf')

for _ in range(N):
    x, y = map(int, input().split())
    x_min, x_max = min(x_min, x), max(x_max, x)
    y_min, y_max = min(y_min, y), max(y_max, y)

x_distance = x_max - x_min
y_distance = y_max - y_min

print(x_distance * y_distance)