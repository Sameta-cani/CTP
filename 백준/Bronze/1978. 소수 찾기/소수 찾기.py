def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

N = int(input())
data = list(map(int, input().split()))
count = sum(is_prime(val) for val in data)

print(count)