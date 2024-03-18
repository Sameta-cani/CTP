N, M = map(int, input().split())

while N != 0 and M != 0:
    print('Yes' if N > M else 'No')
    N, M = map(int, input().split())