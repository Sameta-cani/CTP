word = input()

print(*[c.lower() if c.isupper() else c.upper() for c in word], sep='')