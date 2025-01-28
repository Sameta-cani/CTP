def combination(M, N):
    result = 1
    for i in range(N):
        result *= (M - i)
        result //= i + 1
    return result

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(combination(M, N))