import sys

N = int(sys.stdin.readline().rstrip())
count = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    is_group_word = True
    used_chars = set()
    prev_char = ''

    for char in word:
        if char != prev_char: # 현재 문자가 이전 문자와 다를 경우
            if char in used_chars: # 이미 나타난 문자인지 확인
                is_group_word = False
                break
            used_chars.add(char) # 새로운 문자를 set에 추가
        prev_char = char

    count += is_group_word

print(count)