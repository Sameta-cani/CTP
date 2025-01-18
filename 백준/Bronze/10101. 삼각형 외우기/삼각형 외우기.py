from collections import Counter

angles = [int(input()) for _ in range(3)]

if angles.count(60) == 3:
    print('Equilateral')
else:
    if sum(angles) == 180:
        if len(Counter(angles).most_common()) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print('Error')