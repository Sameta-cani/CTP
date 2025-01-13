M, H = map(int, input().split())
res = 0

for _ in range(int(input())):
    C, B = map(int, input().split())
    res += max(C * M, B * H)
    
print(res)