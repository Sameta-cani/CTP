N = int(input())

cur = 1
i = 0
while cur < N:
    i += 1
    cur += i * 6
    
print(i + 1)