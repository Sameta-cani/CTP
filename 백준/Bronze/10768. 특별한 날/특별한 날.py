month = int(input())
day = int(input())

if (month, day) < (2, 18):
    print("Before")
elif (month, day) > (2, 18):
    print("After")
else:
    print("Special")
