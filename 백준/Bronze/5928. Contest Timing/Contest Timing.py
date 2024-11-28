D, H, M = map(int, input().split())

t = (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)

print(-1 if t < 0 else t)