n, k = map(int, input().split())

# Sum of existing ratings
total = sum(int(input()) for _ in range(k))

max_rating = (total + (n - k) * 3) / n
min_rating = (total + (n - k) * (-3)) / n

print(f'{min_rating:.4f} {max_rating:.4f}')
