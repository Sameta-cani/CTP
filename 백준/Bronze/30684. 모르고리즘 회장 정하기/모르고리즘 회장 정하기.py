import sys

N = int(sys.stdin.readline().rstrip())
names = []
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    if len(name) == 3:
        names.append(name)

names.sort()

sys.stdout.write(names[0])