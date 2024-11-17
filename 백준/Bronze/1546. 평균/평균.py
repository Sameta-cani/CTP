N = int(input())
current_scores = list(map(int, input().split()))

M = max(current_scores)
new_avg = sum(score / M * 100 for score in current_scores) / N

print(new_avg)