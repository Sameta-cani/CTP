import math

N = int(input())

N_fact_reverse = str(math.factorial(N))[::-1]
count = 0

for ch in N_fact_reverse:
    if ch == '0':
        count += 1
    else:
        break

print(count)