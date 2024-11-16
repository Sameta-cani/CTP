base = '12345678'

data = ''.join(list(input().strip().split()))

if data == base:
    print('ascending')
elif data == base[::-1]:
    print('descending')
else:
    print('mixed')