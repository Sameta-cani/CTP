score = input().strip()

res = 0.0

if len(score) == 2:
    res = -ord(score[0]) + 69
    sub = score[1]

    if sub == '+':
        res += 0.3
    elif sub == '-':
        res -= 0.3

print(float(res))