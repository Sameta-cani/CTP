apt = [[0] * 16 for _ in range(16)]
for i in range(1, 16):
    apt[0][i] = i
        
for i in range(1, 16):
    for j in range(1, 16):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    
    print(apt[k][n])