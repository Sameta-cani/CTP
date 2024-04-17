import sys

input = sys.stdin.readline

N = int(input())
coins = sorted(list(map(int, input().split())))

target = 1
for coin in coins:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < coin:
        break
    target += coin

print(target)