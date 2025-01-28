n1 = int(input())
n2 = int(input())

ns = [n1 * int(str(n2)[idx]) for idx in range(2, -1, -1)]

print(*ns, sep='\n')
print(n1 * n2)