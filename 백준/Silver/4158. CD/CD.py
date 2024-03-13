import sys

input = sys.stdin.readline

def count_common_elements(n, m):
    set_n = {int(input().rstrip()) for _ in range(n)}
    set_m = {int(input().rstrip()) for _ in range(m)}
    return len(set_n & set_m)

while True:
    N, M = map(int, input().rstrip().split())
    if N == 0 and M == 0:
        break
    print(count_common_elements(N, M))