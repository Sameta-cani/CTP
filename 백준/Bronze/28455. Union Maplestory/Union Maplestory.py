def get_stat(level):
    if level < 60:
        return 0
    elif level < 100:
        return 1
    elif level < 140:
        return 2
    elif level < 200:
        return 3
    elif level < 250:
        return 4
    else:
        return 5
    
N = int(input())
levels = [int(input()) for _ in range(N)]
stats = list(map(get_stat, levels))

if N < 42:
    print(sum(levels), sum(stats))
else:
    levels_sorted = sorted(levels, reverse=True)
    stats = list(map(get_stat, levels_sorted))
    print(sum(levels_sorted[:42]), sum(stats[:42]))