import sys

pieces = [1, 1, 2, 2, 2, 8]
data = [int(x) for x in sys.stdin.readline().rstrip().split()]

print(*[piece - d for piece, d in zip(pieces, data)])