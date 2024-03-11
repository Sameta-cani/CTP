score_list = []

for i in range(1, 9):
    score_list.append((i, int(input())))

score_list = sorted(score_list, key=lambda x: x[1], reverse=True)[:5]

total = 0
prob_num = []
for val in score_list:
    num, score = val
    total += score
    prob_num.append(num)

print(total)
print(*sorted(prob_num))