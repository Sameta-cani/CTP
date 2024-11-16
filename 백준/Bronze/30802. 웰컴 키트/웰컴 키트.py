N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum((var + T - 1) // T for var in shirts))
print(N // P, N % P)