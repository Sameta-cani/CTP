word = input().strip()

for ch in word:
    print(ch.lower() if ch.isupper() else ch.upper(), end='')