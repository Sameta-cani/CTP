W_score = sum(sorted([int(input()) for _ in range(10)])[-3:])
K_score = sum(sorted([int(input()) for _ in range(10)])[-3:])

print(W_score, K_score)