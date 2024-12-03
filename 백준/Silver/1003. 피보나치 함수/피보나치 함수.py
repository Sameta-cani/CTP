def precompute_fibonacci(n):
    zero_cnt = [1, 0]
    one_cnt = [0, 1]
    for idx in range(2, n + 1):
        zero_cnt.append(zero_cnt[idx - 1] + zero_cnt[idx - 2])
        one_cnt.append(one_cnt[idx - 1] + one_cnt[idx - 2])
    return zero_cnt, one_cnt

zero_cnt, one_cnt = precompute_fibonacci(40)

for _ in range(int(input())):
    N = int(input())
    print(zero_cnt[N], one_cnt[N])