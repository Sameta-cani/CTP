while True:
    sides = sorted(map(int, input().split()))
    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0:
        break
    print('right' if sides[0]**2 + sides[1]**2 == sides[2]**2 else 'wrong')