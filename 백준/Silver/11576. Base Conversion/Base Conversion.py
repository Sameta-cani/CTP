import sys

input = sys.stdin.readline

def convert_base(n: int, base: int) -> None:
    if n == 0:
        return "0"
    
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    
    print(*digits[::-1], sep=' ')

A, B = map(int, input().split()) # A진법 -> B진법
m = int(input()) 
data = list(map(int, input().split()))[::-1]

org = 0
for idx in range(len(data)):
    org += data[idx] * A**idx
    
convert_base(org, B)