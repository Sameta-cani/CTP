L = int(input())
sen = input()

res = 0
power = 1
MOD = 1234567891

for idx in range(L):
    res = (res + (ord(sen[idx]) - ord('a') + 1) * power) % MOD
    power = (power * 31) % MOD
    
print(res)