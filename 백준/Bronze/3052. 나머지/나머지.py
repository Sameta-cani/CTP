import sys

remains = set()

for _ in range(10):
    remains.add(int(sys.stdin.readline().rstrip()) % 42)

print(len(remains))