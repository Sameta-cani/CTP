while True:
    data = sorted(list(map(int, input().split())))
    if sum(data) == 0:
        break

    if data[0]**2 + data[1]**2 == data[2]**2:
        print('right')
    else:
        print('wrong')