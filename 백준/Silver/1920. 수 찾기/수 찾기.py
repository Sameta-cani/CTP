import sys

N = int(sys.stdin.readline().rstrip())
n_array = set(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
m_array = [1 if value in n_array else 0 for value in list(map(int, sys.stdin.readline().rstrip().split()))]

for item in m_array:
    sys.stdout.write(f'{item}\n')