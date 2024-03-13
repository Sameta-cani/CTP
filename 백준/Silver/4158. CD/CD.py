import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

while N != 0 and M != 0:
    N_array = {int(input().rstrip()) for _ in range(N)}
    M_array = {int(input().rstrip()) for _ in range(M)}

    print(len(N_array.intersection(M_array)))

    N, M = map(int, input().rstrip().split())