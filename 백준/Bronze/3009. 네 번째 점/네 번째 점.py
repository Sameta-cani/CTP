from collections import Counter

x_points, y_points = [], []

for _ in range(3):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

# Counter 객체를 사용하여 각 좌표의 빈도수를 계산
x_counter = Counter(x_points)
y_counter = Counter(y_points)

# 빈도수가 1인 좌표를 찾아 출력
x = next(x for x, count in x_counter.items() if count == 1)
y = next(y for y, count in y_counter.items() if count == 1)

print(x, y)