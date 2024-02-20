from collections import Counter

# 입력받은 문자열의 문자별 개수 계산
SC = Counter(input())

# 홀수 번 나타나는 문자 개수 계산
odd_count = sum(1 for count in SC.values() if count % 2 != 0)

# 홀수 번 나타나는 문자가 1개를 초과하면 팰린드롬 불가능
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 중앙에 위치할 문자 초기화
    center_char = ''
    # 팰린드롬의 절반을 구성할 문자열 초기화
    half_p = ''
    for char, count in sorted(SC.items()):
        # 홀수 번 나타나는 문자가 있으면 중앙에 위치시킴
        if count % 2 != 0:
            center_char = char
        # 짝수 번 나타나는 문자와 홀수 번 나타나는 문자의 절반을 half_p에 추가
        half_p += char * (count // 2)

    # 팰린드롬 완성
    p = half_p + center_char + half_p[::-1]

    print(p)