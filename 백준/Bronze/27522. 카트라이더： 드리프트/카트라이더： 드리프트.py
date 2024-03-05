records = []
scores = [10, 8, 6, 5, 4, 3, 2, 1]

for _ in range(8):
    time, team = input().split()
    time = tuple(map(int, time.split(':')))
    record = (time, team)
    records.append(record)

records_sorted = sorted(records, key=lambda x: x[0])
red, blue = 0, 0

for record, score in zip(records_sorted, scores):
    if record[1] == 'R':
        red += score
    else:
        blue += score

print('Red' if red > blue else 'Blue')