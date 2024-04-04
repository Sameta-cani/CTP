def prime_list(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(m, n + 1) if is_prime[i]]

M, N = map(int, input().split())

print(*prime_list(M, N), sep='\n')