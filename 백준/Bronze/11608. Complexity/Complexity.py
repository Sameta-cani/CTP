from collections import Counter

ch_count = Counter(list(input()))

# 문자의 종류가 2개 이하라면, 출력값은 0
if len(ch_count) <= 2:
    print(0)
else:
    # 가장 많이 나타나는 두 문자를 제외한 나머지 문자들의 총 개수를 계산
    total_length = sum(ch_count.values())
    top_two_counts = sum(count for _, count in sorted(ch_count.items(), key=lambda x: x[1], reverse=True)[:2])
    print(total_length - top_two_counts)
