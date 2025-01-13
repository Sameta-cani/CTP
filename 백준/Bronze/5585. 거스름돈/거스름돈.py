coin_types = [500, 100, 50, 10, 5, 1]

N = 1000 - int(input())
cnt = 0

for coin in coin_types:
    cnt += (N // coin)
    N %= coin
    
print(cnt)