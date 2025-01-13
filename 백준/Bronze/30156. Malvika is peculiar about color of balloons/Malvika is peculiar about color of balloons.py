for _ in range(int(input())):
    s = input().strip()
    result = min(s.count('a'), s.count('b'))
    print(result)