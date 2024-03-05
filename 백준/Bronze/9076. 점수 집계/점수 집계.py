T = int(input())

for _ in range(T):
    scores = list(map(int, input().split()))
    scores.remove(max(scores))
    scores.remove(min(scores))
    print(sum(scores) if max(scores) - min(scores) < 4 else 'KIN')