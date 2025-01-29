N = int(input())

x, y = 1, 1
for _ in range(N-1):
    x, y = y, x + y
    
print(x * 2 + y * 2)