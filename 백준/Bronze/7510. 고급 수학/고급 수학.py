for i in range(1, int(input()) + 1):
    a, b, c = sorted(list(map(int, input().split())))
    if a**2 + b**2 == c**2:
        state = 'yes'
    else:
        state = 'no'

    print(f"Scenario #{i}:\n{state}\n")