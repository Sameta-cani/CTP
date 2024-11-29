from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()

mean = round(sum(data) / N)
print(mean)

median = data[N // 2]
print(median)

count = Counter(data)
modes = count.most_common()
max_freq = modes[0][1]

mode_candidates = [num for num, freq in modes if freq == max_freq]
mode_candidates.sort()

if len(mode_candidates) > 1:
    mode = mode_candidates[1]
else:
    mode = mode_candidates[0]
print(mode)

range_ = data[-1] - data[0]
print(range_)