while True:
    var = input()
    if var == '0':
        break
    print("yes" if var == var[::-1] else "no")