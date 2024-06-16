import sys

input = sys.stdin.readline

N, K = map(int, input().split())

str_K = str(K)
cnt = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            cnt += str_K in f"{h:02d}{m:02d}{s:02d}"
            
print(cnt)