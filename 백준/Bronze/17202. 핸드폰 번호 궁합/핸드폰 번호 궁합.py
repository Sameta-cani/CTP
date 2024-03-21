A = input()
B = input()

# A와 B의 각 문자를 차례로 교차하여 결합
result = ''.join(a + b for a, b in zip(A, B))

# 인접한 두 숫자의 합을 계산하며 문자열을 축소
for _ in range(1, 15):
    result = ''.join(str((int(result[i]) + int(result[i + 1])) % 10) for i in range(len(result) - 1))

print(result)