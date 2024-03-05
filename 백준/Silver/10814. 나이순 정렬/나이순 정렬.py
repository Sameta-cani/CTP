N = int(input())

array = [tuple(input().split()) for _ in range(N)]

array.sort(key=lambda x: int(x[0]))

for age, name in array:
    print(f'{age} {name}')