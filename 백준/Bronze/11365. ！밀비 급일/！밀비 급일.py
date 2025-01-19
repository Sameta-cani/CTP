while True:
    sentence = input().strip()
    if sentence == 'END':
        break
    
    print(sentence[::-1])