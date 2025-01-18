N = int(input())
S = input().strip()

cnt = 0
for s in S:
    if s in ('a', 'e', 'i', 'o', 'u'):
        cnt += 1
        
print(cnt)