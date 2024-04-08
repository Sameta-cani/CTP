import sys

input = sys.stdin.readline

H, W, N, M = map(int, input().split())

Hn = H // (N + 1) + (1 if H % (N + 1) != 0 else 0)
Wn = W // (M + 1) + (1 if W % (M + 1) != 0 else 0)

print(Hn * Wn)