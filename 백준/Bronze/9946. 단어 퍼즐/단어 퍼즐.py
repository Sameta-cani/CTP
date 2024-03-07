from collections import Counter

case = 0

while True:
    case += 1
    original = input()
    TMP = input()
    if original == 'END' and TMP == 'END':
        break
    if Counter(original) == Counter(TMP):
        print(f'Case {case}: same')
    else:
        print(f'Case {case}: different')