A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
data = [0] * 10

for val in str(mul):
    data[int(val)] += 1
    
print(*data, sep='\n')