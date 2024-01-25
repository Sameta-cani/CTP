import sys

word = sys.stdin.readline().rstrip()

is_palin = word[:len(word)//2] == word[-(len(word)//2):][::-1]

print(1 if is_palin or len(word) == 1 else 0)
