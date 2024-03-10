N, L, H = map(int, input().split())

array = sorted(list(map(int, input().split())))[L:-H if H else N+1]

print(sum(array) / (N-L-H))