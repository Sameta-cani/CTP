N = int(input())

array = list(set(input() for _ in range(N)))

array.sort(key=lambda x: (len(x), x))

print(*array, sep='\n')