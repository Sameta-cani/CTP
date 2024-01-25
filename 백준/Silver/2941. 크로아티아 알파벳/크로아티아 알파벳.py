import sys

word = input()
croatia = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')

# 크로아티아 알파벳을 한 글자로 대체
for cro in croatia:
    word = word.replace(cro, '*')

print(len(word))