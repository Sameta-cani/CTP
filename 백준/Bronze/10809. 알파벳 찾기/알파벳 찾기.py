res = [-1] * 26

for idx, ch in enumerate(input().strip()):
    if res[ord(ch) - ord('a')] == -1:
        res[ord(ch) - ord('a')] = idx
        
print(*res)