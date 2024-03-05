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

top_levels = sorted(levels, reverse=True)[:min(N, 42)]
top_stats = list(map(get_stat, top_levels))

print(sum(top_levels), sum(top_stats))