import sys

input = sys.stdin.readline

N = int(input())
     
factor = 2
while factor * factor <= N:
    while N % factor == 0:
        print(factor)
        N //= factor
    factor += 1
if N > 1:
    print(N)