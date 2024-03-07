N, L, K = map(int, input().split())

scores = list()

for _ in range(N):
    sub1, sub2 = map(int, input().split())
    if L >= sub1:
        if L >= sub2:
            scores.append(140)
        else:
            scores.append(100)

scores.sort(reverse=True)

print(sum(scores[:K]))