n = int(input())

cond1 = '7' in str(n)
cond2 = n % 7 == 0

if cond1:
    print(3 if cond2 else 2)
else:
    print(1 if cond2 else 0)