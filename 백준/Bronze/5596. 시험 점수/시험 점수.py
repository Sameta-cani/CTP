cond1 = sum(list(map(int, input().split())))
cond2 = sum(list(map(int, input().split())))

print(cond1 if cond1 >= cond2 else cond2)