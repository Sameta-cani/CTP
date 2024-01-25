import sys

# 단어를 입력받고 소문자로 저장
word = sys.stdin.readline().rstrip().lower()

# 입력받은 단어의 유일값만을 저장
unique_word_set = set(word)
# 유일값: 개수 형태인 사전 자료형
unique_word_dict = dict()

# 사전 자료형 입력
for s in unique_word_set:
  unique_word_dict[s] = word.count(s)

# 가장 많이 사용된 알파벳의 개수 초기화
count = 0

# 사전을 하나씩 참조하며
for k, v in unique_word_dict.items():
  # 만약 개수가 가장 많이 사용된 개수와 같다면
  if v == max(unique_word_dict.values()):
    count += 1    # count 증가
    max_word = k    # 가장 많이 사용된 알파벳 저장

# 가장 많이 사용된 알파벳이 여러 개라면
if count > 1:
  sys.stdout.write('?')    # '?' 출력
# 가장 많이 사용된 알파벳이 하나라면
else:
  # 대문자로 출력
  sys.stdout.write(max_word.upper())