N, K = map(int, input().split())

K = min(K, N - K)

res = 1
for i in range(1, K + 1):
    res = res * (N - i + 1) // i
    
print(res)