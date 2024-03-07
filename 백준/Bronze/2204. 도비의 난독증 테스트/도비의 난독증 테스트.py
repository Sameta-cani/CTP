while True:
    n = int(input())
    if n == 0:
        break
    words = [input() for _ in range(n)]
    words_sorted = sorted(words, key=lambda x: x.lower())
    print(words_sorted[0])