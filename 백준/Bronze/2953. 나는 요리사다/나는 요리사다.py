max_idx = 0
max_score = -1

for idx in range(1, 6):
    sum_score = sum(map(int, input().split()))
    if sum_score > max_score:
        max_score = sum_score
        max_idx = idx
        
print(max_idx, max_score)