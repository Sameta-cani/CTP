N, M = map(int, input().split())

if M <= 2:
    print("NEWBIE!")
else:
    if M <= N:
        print("OLDBIE!")
    else:
        print("TLE!")