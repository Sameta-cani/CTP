# 사용할 수 있는 동전의 종료
coin_types = [500, 100, 50, 10, 5, 1]
# 사용할 동전의 수
count = 0

# 거스름돈 계산 (1,000엔에서 입력받은 금액을 뺀 값)
change = 1000 - int(input())

# 각 동전에 대해
for coin in coin_types:
    # 해당 동전으로 거슬러 줄 수 있는 최대 개수를 더함
    count += (change // coin)
    # 거슬러 준 후 남은 금액
    change %= coin

print(count)