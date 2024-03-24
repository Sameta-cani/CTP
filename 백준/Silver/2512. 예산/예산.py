N = int(input())  # 지방의 수
array = list(map(int, input().split()))  # 지방의 예산 요청
M = int(input())  # 총 예산

# 예산 요청의 합이 총 예산보다 작거나 같으면, 요청한 예산을 모두 충족시킬 수 있음
if sum(array) <= M:
    print(max(array))
else:
    start = 0  # 시작값을 0으로 설정
    end = max(array)  # 끝값을 요청된 예산 중 최댓값으로 설정

    while start <= end:
        mid = (start + end) // 2
        total = sum(min(mid, x) for x in array)  # 상한액을 적용한 총 예산 계산

        if total > M:  # 총 예산을 초과하는 경우, 상한액을 낮춤
            end = mid - 1
        else:  # 총 예산 이하인 경우, 상한액을 높임
            result = mid
            start = mid + 1

    print(result)