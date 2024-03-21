def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    count = 0
    d = [0, 1, 1] + [0] * 40
    for i in range(3, 43):
        d[i] = d[i - 1] + d[i - 2]
        count += 1
        if i == n:
            return count

N = int(input())

print(fib(N), fibonacci(N))