sen_cnt = [0] * (ord('z') - ord('a') + 1)

for c in input().strip():
    sen_cnt[(ord(c) - ord('a'))] += 1
    
print(*sen_cnt)