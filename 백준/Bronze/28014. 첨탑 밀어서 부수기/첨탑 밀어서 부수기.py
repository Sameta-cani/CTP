N = int(input())
heights = list(map(int, input().split()))
cnt = 1

for idx in range(1, N):
    if heights[idx - 1] <= heights[idx]:
        cnt += 1
        
print(cnt)