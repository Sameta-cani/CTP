N = int(input())

one, two, three = 0, 0, 0

for value in range(1, N + 1):
    one += value
    three += value**3

print(one, one*one, three, sep='\n')