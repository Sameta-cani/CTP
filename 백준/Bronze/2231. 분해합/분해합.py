N = int(input())

ans = 0
for var in range(1, N + 1):
    if var + sum(map(int, str(var))) == N:
        ans = var
        break
    
print(ans)