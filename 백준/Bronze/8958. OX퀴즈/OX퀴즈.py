for _ in range(int(input())):
    score = 0
    current_streak = 0
    for ch in input().strip():
        if ch == 'O':
            current_streak += 1
            score += current_streak
        elif ch == 'X':
            current_streak = 0
    print(score) 