N = int(input())
# 막대의 길이
X = sorted(list(map(int, input().split())))
# 상자 크기
Y = sorted(list(map(int, input().split())))

is_clear = True

for x, y in zip(X, Y):
    if x > y:
        is_clear = False
        break

print("DA" if is_clear else "NE")