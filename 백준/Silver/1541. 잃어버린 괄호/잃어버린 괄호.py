import re

# 입력된 수식 받기
formula = input()

# '-' 연산자로 문자열을 분리
parts = formula.split('-')

# 첫 번째 부분(처음 '-' 연산자가 나오기 전까지)을 계산
result = sum(map(int, re.findall(r'\d+', parts[0])))

# 이후 부분에서, 각 '-' 연산자로 분리된 부분의 합을 전체 결과에서 빼기
for part in parts[1:]:
    result -= sum(map(int, re.findall(r'\d+', part)))

print(result)
