N = int(input())
array = sorted(list(map(int, input().split())))

min_value = 0

for val in array:
    if val - min_value == 1:
        min_value = val

print(min_value + 1)