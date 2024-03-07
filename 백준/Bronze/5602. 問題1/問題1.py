N, M = map(int, input().split())

votes = [0] * M

for _ in range(N):
    vote = list(map(int, input().split()))
    for i in range(M):
        votes[i] += vote[i]

# 각 후보의 인덱스와 투표수를 튜플로 묶어 리스트 생성
votes_with_index = [(index + 1, vote) for index, vote in enumerate(votes)]

# 투표수에 따라 내림차순으로 정렬
sorted_votes = sorted(votes_with_index, key=lambda x: x[1], reverse=True)

# 정렬된 후보의 인덱스만 추출하여 출력
sorted_indexes = [index for index, _ in sorted_votes]
print(*sorted_indexes)