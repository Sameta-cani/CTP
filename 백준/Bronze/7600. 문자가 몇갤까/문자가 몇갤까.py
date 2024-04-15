import sys

input = sys.stdin.readline

while True:
    sentence = input().lower().rstrip() # 모두 소문자로 바꾼 후, 뒤에 개행 문자를 제거
    if sentence == '#': # 입력 받은 문자열이 '#' 이라면 종료
        break

    unq_alphabet = {ch for ch in sentence if ch.isalpha()} # 글자 하나씩 검사하면서 알파벳인지 확인 후 추가
    print(len(unq_alphabet)) # unq_alphabet에 있는 원소의 개수