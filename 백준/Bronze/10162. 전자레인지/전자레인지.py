button_types = [300, 60, 10]
T = int(input())

if T % 10 != 0:
    print(-1)
else:
    for button in button_types:
        print(T // button, end=' ')
        T %= button