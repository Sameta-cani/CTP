scores = list(map(int, input().split()))

if sum(scores) >= 100:
    print("OK")
else:
    min_idx = 0
    min_score = float("INF")
    for i in range(3):
        if scores[i] < min_score:
            min_idx = i
            min_score = scores[i]
            
    names = ["Soongsil", "Korea", "Hanyang"]
    print(names[min_idx])