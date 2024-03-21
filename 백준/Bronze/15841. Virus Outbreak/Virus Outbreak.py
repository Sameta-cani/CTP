max_hour = 490

d = [0] * 491
d[1] = 1
d[2] = 1

for i in range(3, max_hour + 1):
    d[i] = d[i - 1] + d[i - 2]

hour = int(input())

while hour != -1:
    print(f'Hour {hour}: {d[hour]} cow(s) affected')
    hour = int(input())