import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    R = int(R)
    repeated_str = ''.join([ch * R for ch in S])
    print(repeated_str)