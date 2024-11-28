S = input().strip()

for ch in S:
    cnt = sum(int(digit) for digit in str(ord(ch)))
    print(ch * cnt)