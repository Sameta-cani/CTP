data = set(input() for _ in range(int(input())))

data = sorted(data, key=lambda x: (len(x), x))

print('\n'.join(data))