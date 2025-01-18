for _ in range(int(input())):
    pw = input().strip()
    print('yes' if 6 <= len(pw) <= 9 else 'no')