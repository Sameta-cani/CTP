for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{n} is {state}')