import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    last_submission = [0] * (n + 1)
    submissions_count = [0] * (n + 1)
    scores = [[0] * (k + 1) for _ in range(n + 1)]

    for entry in range(m):
        team_id, problem_id, score = map(int, input().split())
        if scores[team_id][problem_id] < score:
            scores[team_id][problem_id] = score
        submissions_count[team_id] += 1
        last_submission[team_id] = entry
    
    rank = []
    for team_id in range(1, n + 1):
        total_score = sum(scores[team_id])
        rank.append((total_score, -submissions_count[team_id], -last_submission[team_id], team_id))
    
    rank.sort(reverse=True)
    for idx, (score, count, last_sub, team) in enumerate(rank, 1):
        if team == t:
            print(idx)
            break