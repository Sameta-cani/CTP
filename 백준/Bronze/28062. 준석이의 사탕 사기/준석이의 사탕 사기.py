import sys

input = sys.stdin.readline

N = int(input())
array = sorted(list(map(int, input().split())))
total = sum(array)

# 짝수 => ok
# 홀수 - 짝수 = 홀수
# 홀수 - 홀수 = 짝

if total % 2 == 0:
    print(total)
else:
    for value in array:
        ans = total - value
        if ans % 2 == 0:
            print(ans)
            break