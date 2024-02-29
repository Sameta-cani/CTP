def get_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

while True:
    n = int(input())
    if n == -1:
        break
    divisors = sorted(get_divisors(n))
    if sum(divisors) == n:
        print(f'{n} = ', end='')
        print(*divisors, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')