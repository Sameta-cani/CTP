import sys

a, b = map(int, sys.stdin.readline().split())

op = '>' if a > b else ('==' if a == b else '<')

sys.stdout.write(op)