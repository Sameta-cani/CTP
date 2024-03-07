from collections import Counter
import sys

case = 0

while True:
    case += 1
    original = sys.stdin.readline().rstrip()
    TMP = input()
    if original == 'END' and TMP == 'END':
        break
    if Counter(original) == Counter(TMP):
        print(f'Case {case}: same')
    else:
        print(f'Case {case}: different')