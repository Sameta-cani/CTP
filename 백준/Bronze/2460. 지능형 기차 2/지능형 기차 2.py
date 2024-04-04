max_value = -int(1e9)

current = 0

for _ in range(10):
    a, b = map(int, input().split())
    current = current - a + b
    max_value = max(max_value, current)

print(max_value)