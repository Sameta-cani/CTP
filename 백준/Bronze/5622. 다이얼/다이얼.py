dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input().strip()

res = 0
for ch in word:
    for dial in dials:
        if ch in dial:
            res += dials.index(dial) + 3
            
print(res)
