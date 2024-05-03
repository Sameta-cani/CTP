import sys

input = sys.stdin.readline

def check(num):
    for i in range(1, 46):
        for j in range(1, 46):
            for k in range(1, 46):
                if dp[i] + dp[j] + dp[k] == num:
                    return 1
    return 0

dp = [0] * 1000

for i in range(1, 1000):
    dp[i] = dp[i - 1] + i

for _ in range(int(input())):
    print(check(int(input())))