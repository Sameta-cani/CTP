N, K = map(int, input().split())

factors = set()

for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        factors.add(i)
        factors.add(N//i)

sorted_factors = sorted(factors)

print(sorted_factors[K-1] if K <= len(sorted_factors) else 0)