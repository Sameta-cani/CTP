import sys

N = int(input())

array = [tuple(sys.stdin.readline().rstrip().split()) for _ in range(N)]

array.sort(key=lambda x: int(x[0]))

for age, name in array:
    sys.stdout.write(f'{age} {name}\n')