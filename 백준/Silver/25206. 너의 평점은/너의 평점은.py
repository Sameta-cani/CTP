import sys

subject_rating = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
total_grade_points = 0
total_credits = 0

for _ in range(20):
    score, grade = sys.stdin.readline().rstrip().split()[-2:]
    if grade == "P":  # 성적이 'P'인 경우 제외
        continue
    score = float(score)
    total_grade_points += score * subject_rating[grade]
    total_credits += score

average_grade = total_grade_points / total_credits
print(average_grade)
