def is_palindrome(word):
    is_palin = True
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - (i + 1)]:
            is_palin = False
            break
    return is_palin

N = input()

while N != '0':
    print('yes' if is_palindrome(N) else 'no')
    N = input()