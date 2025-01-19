while True:
    sentence = input().strip().lower()
    if sentence == '#':
        break
    
    cnt = 0
    for vowel in ('a', 'e', 'i', 'o', 'u'):
        cnt += sentence.count(vowel)
        
    print(cnt)