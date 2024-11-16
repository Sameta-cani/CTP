N = int(input())

for var in range(max(1, N - len(str(N)) * 9), N):
    if var + sum(int(digit) for digit in str(var)) == N:
        print(var)
        break
    
else:
    print(0)