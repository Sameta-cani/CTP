P = int(input())

for p in range(1, P+1):
    n, m = map(int, input().split())
    candidates = {input(): 0 for _ in range(n)}

    for _ in range(m):
        X, R, C = input().split()
        candidates[X] += int(R)

    max_candidates = [(c, v) for c, v in candidates.items() if v == max(candidates.values())]
    
    if len(max_candidates) > 1:
        print(f'VOTE {p}: THERE IS A DILEMMA')
    else:
        c, v = max_candidates[0]
        print(f'VOTE {p}: THE WINNER IS {c} {v}')