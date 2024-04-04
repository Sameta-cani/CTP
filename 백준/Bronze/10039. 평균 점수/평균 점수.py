array = [int(input()) for _ in range(5)]

print(sum([value if value >= 40 else 40 for value in array]) // 5)