N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for idx in range(N):
    if B[idx] > A[idx]:
        res += B[idx] - A[idx]
        
print(res)