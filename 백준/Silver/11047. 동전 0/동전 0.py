import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for coin in coins[::-1]:
    cnt += K // coin
    K %= coin

print(cnt)