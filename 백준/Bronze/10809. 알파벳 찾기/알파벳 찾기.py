import sys

S = sys.stdin.readline().rstrip()
alphabet_positions = [S.find(chr(i)) for i in range(97, 123)]

print(*alphabet_positions)