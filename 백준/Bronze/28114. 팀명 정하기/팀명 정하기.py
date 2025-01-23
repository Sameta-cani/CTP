import sys

input = sys.stdin.readline

data = [input().strip().split() for _ in range(3)]

sorted_by_second = sorted(data, key=lambda x: int(x[1]))
print(''.join(str(int(row[1]) % 100) for row in sorted_by_second))

sorted_by_first_dec = sorted(data, key=lambda x: int(x[0]), reverse=True)
print(''.join(row[2][0] for row in sorted_by_first_dec))
