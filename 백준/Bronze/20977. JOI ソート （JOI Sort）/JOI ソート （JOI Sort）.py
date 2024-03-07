import sys

N = int(sys.stdin.readline().rstrip())

data = sys.stdin.readline().rstrip()

# 'I'를 제외한 문자들만 정렬
sorted_data = sorted(filter(lambda x: x!= 'I', data))

# 'I'의 개수를 계산
count_I = data.count('I')

# 'I'가 아닌 문자들이 정렬된 리스트 끝에 'I' 개수만틈 추가
result = ''.join(sorted_data) + 'I' * count_I

sys.stdout.write(result)