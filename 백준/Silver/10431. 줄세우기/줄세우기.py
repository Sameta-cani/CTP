import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().split()))
    T, array = data[0], data[1:]
    total = 0

    for idx in range(1, 20):
        current_value = array[idx]
        count = 0

        for j in range(idx - 1, -1, -1):
            if current_value < array[j]:
                count += 1

        total += count

    print(T, total)