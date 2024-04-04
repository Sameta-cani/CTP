def prime_list(n):
    is_prime = [True] * (n + 1)

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i + i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

M, N = map(int, input().split())

for value in prime_list(N):
    if value >= M:
        print(value)