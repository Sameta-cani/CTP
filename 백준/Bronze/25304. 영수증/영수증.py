X = int(input())

res = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    res += a * b
    
print("Yes" if X == res else "No")