N = int(input())

result = 666
cnt = 1

while cnt < N:
    result += 1
    if '666' in str(result):
        cnt += 1
        
print(result)