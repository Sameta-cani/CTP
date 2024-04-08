import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    print(sum(list(range(1, n + 1))))