N = int(input())
count = 0

for _ in range(N):
    word = input()
    is_groupword = True
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]: # 현재 문자와 다음 문자가 다르면
            if word[i] in word[i + 1:]: # 현재 문자가 이후 문자열에 나타난다면 그룹 단어가 아님
                is_groupword = False
                break
    count += is_groupword

print(count)