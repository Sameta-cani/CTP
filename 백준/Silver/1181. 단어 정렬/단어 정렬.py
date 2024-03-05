import sys

N = int(input())

array = list(set(sys.stdin.readline().rstrip() for _ in range(N)))

array.sort(key=lambda x: (len(x), x))

for item in array:
    sys.stdout.write(item + '\n')