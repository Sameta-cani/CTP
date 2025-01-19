scores = [int(input()) for _ in range(6)]

ans = sum(scores) - min(scores[:4]) - min(scores[4:])

print(ans)